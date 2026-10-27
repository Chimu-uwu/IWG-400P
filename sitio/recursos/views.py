
from django.shortcuts import render


def vista_biblioteca(request):

    # =========================================
    # 1. RECURSOS EDUCATIVOS
    # =========================================

    # Cada diccionario representa un recurso.
    # Más adelante, estos datos podrán venir
    # desde los modelos de Django.

    recursos = [
        {
            "titulo": "Números y operaciones",
            "tema": "numeros",
            "tipo": "Lecciones",
            "descripcion": (
                "Repasa operaciones matemáticas, "
                "fracciones, potencias y raíces."
            ),
            "url": "https://es.khanacademy.org/math",
        },
        {
            "titulo": "Fundamentos de Álgebra",
            "tema": "algebra",
            "tipo": "Ejercicios",
            "descripcion": (
                "Practica expresiones algebraicas, "
                "ecuaciones y otros fundamentos."
            ),
            "url": "https://es.khanacademy.org/math",
        },
        {
            "titulo": "Gráficas de funciones",
            "tema": "funciones",
            "tipo": "Herramienta interactiva",
            "descripcion": (
                "Explora gráficas, ecuaciones "
                "y el comportamiento de funciones."
            ),
            "url": "https://www.geogebra.org/graphing",
        },
        {
            "titulo": "Geometría interactiva",
            "tema": "geometria",
            "tipo": "Herramienta interactiva",
            "descripcion": (
                "Construye figuras, analiza ángulos "
                "y estudia propiedades geométricas."
            ),
            "url": "https://www.geogebra.org/geometry",
        },
        {
            "titulo": "Precálculo y Trigonometría",
            "tema": "trigonometria",
            "tipo": "Libro digital",
            "descripcion": (
                "Consulta capítulos sobre funciones "
                "trigonométricas e identidades."
            ),
            "url": (
                "https://espanol.libretexts.org/"
                "Bookshelves/Matematicas/"
                "Precalculo_y_Trigonometria/"
                "Prec%C3%A1lculo_%28OpenStax%29"
            ),
        },
    ]

    # =========================================
    # 2. TEMAS DISPONIBLES
    # =========================================

    temas = {
        "todos": "Todos",
        "numeros": "Números y operaciones",
        "algebra": "Álgebra",
        "funciones": "Funciones",
        "geometria": "Geometría",
        "trigonometria": "Trigonometría",
    }

    # =========================================
    # 3. OBTENER EL FILTRO SELECCIONADO
    # =========================================

    tema_actual = request.GET.get("tema", "todos")

    # Si el tema no existe, mostramos todos.
    if tema_actual not in temas:
        tema_actual = "todos"

    # =========================================
    # 4. FILTRAR LOS RECURSOS
    # =========================================

    if tema_actual == "todos":
        recursos_filtrados = recursos
    else:
        recursos_filtrados = [
            recurso
            for recurso in recursos
            if recurso["tema"] == tema_actual
        ]

    # =========================================
    # 5. ENVIAR DATOS AL HTML
    # =========================================

    contexto = {
        "recursos": recursos_filtrados,
        "temas": temas,
        "tema_actual": tema_actual,
        "cantidad": len(recursos_filtrados),
    }

    return render(
        request,
        "recursos/biblioteca.html",
        contexto
    )
