import json

from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from core.models import Ejercicio

# Asignatura (URL) -> (nombre visible, códigos de materia en la base de datos).
# Matemáticas agrupa Álgebra (ALG) y Cálculo (CAL), tal como viene en el CSV.
ASIGNATURAS = {
    'matematicas': ('Matemáticas', ['ALG', 'CAL']),
    'fisica': ('Física', ['FIS']),
}

CLAVE_SESION = 'ultimo_resultado'


def _asignatura_o_404(codigo):
    if codigo not in ASIGNATURAS:
        raise Http404("Asignatura no disponible")
    nombre, materias = ASIGNATURAS[codigo]
    return nombre, materias


def vista_inicio(request):
    return render(request, 'diagnostico/inicio.html')


def vista_diagnostico(request):
    return render(request, 'diagnostico/evaluacion.html')


def vista_instrucciones(request, asignatura):
    nombre, materias = _asignatura_o_404(asignatura)
    return render(request, 'diagnostico/instrucciones.html', {
        'asignatura': nombre,
        'codigo_asignatura': asignatura,
        'total_preguntas': Ejercicio.objects.filter(materia__in=materias).count(),
    })


def vista_preguntas(request, asignatura):
    nombre, materias = _asignatura_o_404(asignatura)

    # IMPORTANTE: no se envía la respuesta correcta al navegador;
    # la corrección se hace en el servidor (vista_calificar).
    preguntas = [
        {
            'id': e.id,
            'tema': e.tema,
            'enunciado': e.enunciado,
            'alternativas': e.alternativas,
        }
        for e in Ejercicio.objects.filter(materia__in=materias).order_by('nivel_dificultad', 'codigo')
    ]
    return render(request, 'diagnostico/preguntas.html', {
        'asignatura': nombre,
        'codigo_asignatura': asignatura,
        'preguntas': preguntas,
    })


@require_POST
def vista_calificar(request, asignatura):
    """Recibe {"respuestas": {"<id ejercicio>": <índice 0-3>}} y devuelve el resumen por tema."""
    nombre, materias = _asignatura_o_404(asignatura)

    try:
        enviadas = json.loads(request.body or '{}').get('respuestas', {})
        if not isinstance(enviadas, dict):
            raise ValueError
    except ValueError:
        return JsonResponse({'error': 'Formato de respuestas inválido'}, status=400)

    por_tema = {}
    fallidos = []
    for e in Ejercicio.objects.filter(materia__in=materias):
        dato = por_tema.setdefault(e.tema or 'Sin tema', {'correctas': 0, 'total': 0})
        dato['total'] += 1
        elegida = enviadas.get(str(e.id))
        # índice 0-3 -> letra A-D; sin responder cuenta como incorrecta
        letra = 'ABCD'[elegida] if isinstance(elegida, int) and 0 <= elegida <= 3 else None
        if letra == e.respuesta_correcta:
            dato['correctas'] += 1
        else:
            fallidos.append(e.id)

    resumen = sorted(
        ({'tema': t, 'correctas': d['correctas'], 'total': d['total'],
          'porcentaje': round(100 * d['correctas'] / d['total'])}
         for t, d in por_tema.items()),
        key=lambda x: x['porcentaje'],
    )
    total = sum(d['total'] for d in por_tema.values())
    correctas = sum(d['correctas'] for d in por_tema.values())

    # Se guarda en la sesión para que la ruta de estudio (app recursos) lo use.
    request.session[CLAVE_SESION] = {
        'asignatura': asignatura,
        'correctas': correctas,
        'total': total,
        'por_tema': resumen,
        'fallidos': fallidos,
    }
    return JsonResponse({'correctas': correctas, 'total': total, 'por_tema': resumen})
