import json
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db import transaction
from core.models import Resultado, EvaluacionDiagnostica
import random
from collections import defaultdict

from core.models import Ejercicio


# Asignaturas las urls (nombre visible, códigos de materia en la base de datos).
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

@login_required
def vista_inicio(request):
    return render(request, 'diagnostico/inicio.html')

@login_required
def vista_diagnostico(request):
    return render(request, 'diagnostico/evaluacion.html')

@login_required
def vista_instrucciones(request, asignatura):
    nombre, materias = _asignatura_o_404(asignatura)
    return render(request, 'diagnostico/instrucciones.html', {
        'asignatura': nombre,
        'codigo_asignatura': asignatura,
        'total_preguntas': Ejercicio.objects.filter(materia__in=materias).count(),
    })

@login_required
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

@login_required
@require_POST
def vista_calificar(request, asignatura):
    """Recibe {"respuestas": {"<id ejercicio>": <índice 0-3>}} y devuelve el resumen por tema."""
    nombre, materias = _asignatura_o_404(asignatura)

    # Recuperar las preguntas del intento
    ids_preguntas = request.session.get(f'preguntas_{asignatura}')

    if not ids_preguntas:return JsonResponse({'error': 'No hay una evaluación iniciada'},status=400)

    try:
        enviadas = json.loads(request.body or '{}').get('respuestas', {})
        if not isinstance(enviadas, dict):
            raise ValueError
    except ValueError:
        return JsonResponse({'error': 'Formato de respuestas inválido'}, status=400)

    por_tema = {}
    fallidos = []
    for e in Ejercicio.objects.filter(id__in=ids_preguntas,materia__in=materias):
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

    # GUARDAR RESULTADO EN LA BASE DE DATOS
    porcentaje = round(
        (correctas / total) * 100, 2
    ) if total > 0 else 0

    # Obtener o crear la evaluación de Matemáticas
    evaluacion, creada = EvaluacionDiagnostica.objects.get_or_create(
        titulo='Diagnóstico de Matemáticas',
        materia='MAT'
    )

    #guarda el resultado
    resultado = Resultado.objects.create(
        usuario=request.user,
        evaluacion=evaluacion,
        respuestas_correctas=correctas,
        total_preguntas=total,
        puntaje_obtenido=porcentaje,
        resultados_detallados={
            'por_tema': resumen,
            'fallidos': fallidos
        }

    )

    # Se guarda en la sesión para que la ruta de estudio (app recursos) lo use.
    request.session[CLAVE_SESION] = {
        'asignatura': asignatura,
        'correctas': correctas,
        'total': total,
        'por_tema': resumen,
        'fallidos': fallidos,
    }
    # Evitar corregir nuevamente el mismo intento
    request.session.pop(f'preguntas_{asignatura}',None)
    return JsonResponse({'correctas': correctas, 'total': total, 'por_tema': resumen})



@login_required
# HISTORIAL DE RESULTADOS
def vista_resultados(request):

    # Recuperar resultados del usuario conectado
    resultados = Resultado.objects.filter(
        usuario=request.user
    ).select_related(
        'evaluacion'
    ).order_by('-fecha_rendicion')

    # Obtener el resultado más reciente
    ultimo_resultado = resultados.first()

    temas = []
    temas_reforzar = []
    incorrectas = 0

    if ultimo_resultado:

        incorrectas = (
            ultimo_resultado.total_preguntas
            - ultimo_resultado.respuestas_correctas
        )

        detalles = ultimo_resultado.resultados_detallados or {}

        temas = detalles.get('por_tema', [])

        temas_reforzar = [
            tema['tema']
            for tema in temas
            if tema['porcentaje'] <= 50
        ]

    return render(
        request,
        'diagnostico/resultados.html',
        {
            'resultados': resultados,
            'ultimo_resultado': ultimo_resultado,
            'temas': temas,
            'temas_reforzar': temas_reforzar,
            'incorrectas': incorrectas,
        }
    )

@login_required
def vista_preguntas(request, asignatura):

    nombre, materias = _asignatura_o_404(asignatura)

    # Obtener preguntas disponibles
    ejercicios = list(
        Ejercicio.objects.filter(materia__in=materias)
    )

    # Agrupar ejercicios por tema
    ejercicios_por_tema = defaultdict(list)

    for ejercicio in ejercicios:
        ejercicios_por_tema[ejercicio.tema].append(ejercicio)

    # Seleccionar 7 preguntas aleatorias de cada tema
    seleccionadas = []

    for tema, preguntas_tema in ejercicios_por_tema.items():

        cantidad = min(7, len(preguntas_tema))

        seleccionadas.extend(
            random.sample(preguntas_tema, cantidad)
        )

    # Mezclar el orden de las preguntas
    random.shuffle(seleccionadas)

    # Guardar identificadores del intento en sesión
    request.session[f'preguntas_{asignatura}'] = [
        ejercicio.id for ejercicio in seleccionadas
    ]

    # Preparar preguntas para JavaScript
    preguntas = [
        {
            'id': e.id,
            'tema': e.tema,
            'enunciado': e.enunciado,
            'alternativas': e.alternativas,
        }
        for e in seleccionadas
    ]

    return render(request,'diagnostico/preguntas.html',
        {
            'asignatura': nombre,
            'codigo_asignatura': asignatura,
            'preguntas': preguntas,
        }
    )