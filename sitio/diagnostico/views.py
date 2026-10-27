
from django.shortcuts import render

def vista_inicio(request):
    return render(request, 'diagnostico/inicio.html')

def vista_diagnostico(request):
    return render(request, 'diagnostico/evaluacion.html')


def vista_instrucciones(request, asignatura):

    # Diccionario con las asignaturas disponibles
    asignaturas = {
        'matematicas': 'Matemáticas',
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


def vista_resultados(request):

    # =====================================
    # 1. RESPUESTAS FICTICIAS
    # =====================================

    # True = respuesta correcta
    # False = respuesta incorrecta

    respuestas = {
        "Números y operaciones": [
            True, True, True, True
        ],

        "Álgebra": [
            True, False, True, True
        ],

        "Funciones": [
            True, False, True, False
        ],

        "Geometría": [
            True, True, True, True
        ],

        "Trigonometría": [
            False, True, False, True
        ],
    }

    # =====================================
    # 2. VARIABLES PARA LOS RESULTADOS
    # =====================================

    temas = []
    temas_reforzar = []

    correctas = 0
    total = 0

    # =====================================
    # 3. RECORRER CADA TEMA
    # =====================================

    for nombre, respuestas_tema in respuestas.items():

        cantidad = len(respuestas_tema)
        aciertos = sum(respuestas_tema)

        porcentaje_tema = (
            round(aciertos / cantidad * 100)
            if cantidad > 0 else 0
        )

        temas.append({
            "nombre": nombre,
            "porcentaje": porcentaje_tema,
            "correctas": aciertos,
            "total": cantidad,
        })

        # Sumamos al resultado general
        correctas += aciertos
        total += cantidad

        # Recomendaciones de refuerzo
        if porcentaje_tema <= 50:
            temas_reforzar.append(nombre)

    # =====================================
    # 4. RESULTADO GENERAL
    # =====================================

    incorrectas = total - correctas

    porcentaje = (
        round(correctas / total * 100)
        if total > 0 else 0
    )

    # =====================================
    # 5. ENVIAR LOS DATOS AL HTML
    # =====================================

    contexto = {
        "asignatura": "Matemáticas",
        "correctas": correctas,
        "incorrectas": incorrectas,
        "total": total,
        "porcentaje": porcentaje,
        "temas": temas,
        "temas_reforzar": temas_reforzar,
    }

    return render(
        request,
        "diagnostico/resultados.html",
        contexto
    )

