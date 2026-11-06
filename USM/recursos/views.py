from django.db.models import Max, Q
from django.shortcuts import redirect, render
from core.models import Ejercicio, Recurso
from diagnostico.views import ASIGNATURAS, CLAVE_SESION
from django.contrib.auth.decorators import login_required
from core.models import Recurso


@login_required
def vista_almacen(request):
    tema = request.GET.get("tema", "todos")

    recursos = Recurso.objects.all().order_by("tema", "titulo")

    if tema != "todos":
        recursos = recursos.filter(tema=tema)

    return render(request, "recursos/almacen.html", {
        "recursos": recursos,
        "tema_actual": tema,
    })

def _estado(porcentaje):
    if porcentaje < 50:
        return 'reforzar', 'Reforzar'
    if porcentaje < 80:
        return 'repasar', 'Repasar'
    return 'dominado', 'Dominado'


def ruta_estudio(request):
    """Roadmap: temas ordenados de más débil a más fuerte, con retroalimentación y recursos."""
    res = request.session.get(CLAVE_SESION)
    if not res:
        return redirect('evaluacion')

    materias = ASIGNATURAS[res['asignatura']][1]
    fallidos = Ejercicio.objects.filter(id__in=res['fallidos'])

    temas = []
    for t in res['por_tema']:
        clave, etiqueta = _estado(t['porcentaje'])
        fallos_tema = fallidos.filter(tema=t['tema'])
        nivel_max = fallos_tema.aggregate(m=Max('nivel_dificultad'))['m']

        recursos = []
        if nivel_max:  # solo se recomiendan recursos donde hubo errores
            recursos = Recurso.objects.filter(
                Q(tema=t['tema']) | Q(tema=''),
                materia__in=materias,
                nivel_dificultad__lte=nivel_max,
            ).order_by('nivel_dificultad', 'titulo')

        temas.append({**t, 'estado': clave, 'etiqueta': etiqueta,
                      'fallos': fallos_tema, 'recursos': recursos})

    return render(request, 'recursos/ruta_estudio.html', {
        'asignatura': ASIGNATURAS[res['asignatura']][0],
        'correctas': res['correctas'],
        'total': res['total'],
        'temas': temas,
    })
