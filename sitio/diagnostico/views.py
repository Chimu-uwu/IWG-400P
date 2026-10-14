
from django.shortcuts import render

def vista_inicio(request):
    return render(request, 'diagnostico/inicio.html')

def vista_diagnostico(request):
    return render(request, 'diagnostico/evaluacion.html')


def vista_instrucciones(request, asignatura):

    # Diccionario con las asignaturas disponibles
    asignaturas = {
        'matematicas': 'Matemáticas',
        'fisica': 'Física',
    }

    # Verificamos que la asignatura exista
    if asignatura not in asignaturas:
        from django.http import Http404
        raise Http404("Asignatura no disponible")

    # Datos que enviaremos al HTML
    contexto = {
        'asignatura': asignaturas[asignatura],
        'codigo_asignatura': asignatura,
    }

    # Mostramos la plantilla con sus datos
    return render(
        request,
        'diagnostico/instrucciones.html',
        contexto
    )


def vista_preguntas(request, asignatura):

    # Asignaturas disponibles
    asignaturas = {
        'matematicas': 'Matemáticas',
        'fisica': 'Física',
    }

    # Impedimos el acceso a asignaturas inexistentes
    if asignatura not in asignaturas:
        from django.http import Http404
        raise Http404("Asignatura no disponible")

    # Información enviada al HTML
    contexto = {
        'asignatura': asignaturas[asignatura],
        'codigo_asignatura': asignatura,
    }

    return render(
        request,
        'diagnostico/preguntas.html',
        contexto
    )
