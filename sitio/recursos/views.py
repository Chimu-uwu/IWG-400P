from django.shortcuts import render


def vista_biblioteca(request):

    # =========================================
    # 1. RECURSOS EDUCATIVOS
    # =========================================

    # Cada diccionario representa un recurso.
    # Más adelante, estos datos podrán venir
    # desde los modelos de Django.

    recursos = [
        # --- RECURSOS ORIGINALES ---
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
        # --- VIDEOS DE YOUTUBE ---
        {
            "titulo": "Video 1: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Suma y resta.",
            "url": "https://www.youtube.com/watch?v=v4h6KZkQ1Q0&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA",
        },
        {
            "titulo": "Video 2: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Suma, resta y multiplicación.",
            "url": "https://www.youtube.com/watch?v=VvvtknaN0j0&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA&index=3",
        },
        {
            "titulo": "Video 1: Álgebra",
            "tema": "algebra",
            "tipo": "Video",
            "descripcion": "Término y sus partes.",
            "url": "https://www.youtube.com/watch?v=a-H0e27KNUk&list=PLeySRPnY35dGSJYCRn7tD1mVatw3MrdIm&index=2",
        },
        {
            "titulo": "Video 2: Álgebra",
            "tema": "algebra",
            "tipo": "Video",
            "descripcion": "Términos semejantes.",
            "url": "https://www.youtube.com/watch?v=_0vaN7XMUsg&list=PLeySRPnY35dGSJYCRn7tD1mVatw3MrdIm&index=3",
        },
        {
            "titulo": "Video 1: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "¿Qué es una función?.",
            "url": "https://www.youtube.com/watch?v=HAeSkQH1C-I&list=PLeySRPnY35dGfEuNGbQmymhiQF4oTUIMb",
        },
        {
            "titulo": "Video 2: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "Función inyectiva, sobreyectiva y biyectiva.",
            "url": "https://www.youtube.com/watch?v=xhBWUbY1VrM&list=PLeySRPnY35dGfEuNGbQmymhiQF4oTUIMb&index=2",
        },
        {
            "titulo": "Video 1: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "Teorema de Pitágoras.",
            "url": "https://www.youtube.com/watch?v=w6nh99v3r4A&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi",
        },
        {
            "titulo": "Video 2: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "Ángulo entre paralelas y secantes.",
            "url": "https://www.youtube.com/watch?v=5_ky4mWpSA4&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi&index=3",
        },
        {
            "titulo": "Video 1: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Razones trigonométricas en triángulo rectángulo.",
            "url": "https://www.youtube.com/watch?v=7pUi5lvLf7c",
        },
        {
            "titulo": "Video 2: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Cateto opuesto, cateto adyacente e hipotenusa.",
            "url": "https://www.youtube.com/watch?v=FUMlQtJfrHo",
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