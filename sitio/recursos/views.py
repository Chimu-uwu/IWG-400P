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
            "descripcion": "Suma y resta | Ejemplo 1",
            "url": "https://www.youtube.com/watch?v=v4h6KZkQ1Q0&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA",
        },
        {
            "titulo": "Video 2: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Suma y resta | Ejemplo 2.",
            "url": "https://www.youtube.com/watch?v=lTpbx63UK6M&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA&index=2",
        },
        {
            "titulo": "Video 1: Álgebra",
            "tema": "algebra",
            "tipo": "Video",
            "descripcion": "Qué es el Álgebra.",
            "url": "https://www.youtube.com/watch?v=4LouAWcajJs&list=PLeySRPnY35dGSJYCRn7tD1mVatw3MrdIm&index=1",
        },
        {
            "titulo": "Video 2: Álgebra",
            "tema": "algebra",
            "tipo": "Video",
            "descripcion": "Qué es un término y sus partes.",
            "url": "https://www.youtube.com/watch?v=a-H0e27KNUk&list=PLeySRPnY35dGSJYCRn7tD1mVatw3MrdIm&index=2",
        },
        {
            "titulo": "Video 1: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "¿Qué es una Función?.",
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
            "descripcion": "TEOREMA DE PITÁGORAS 📐 Fórmula, Demostración y Ejemplos.",
            "url": "https://www.youtube.com/watch?v=w6nh99v3r4A&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi",
        },
        {
            "titulo": "Video 2: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "TEOREMA DE PITÁGORAS 📐 Aplicación en Figuras Planas.",
            "url": "https://www.youtube.com/watch?v=WXRdDDo1xbA&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi&index=2",
        },
        {
            "titulo": "Video 1: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "¿Qué son las razones trigonométricas?.",
            "url": "https://www.youtube.com/watch?v=7pUi5lvLf7c&list=PLeySRPnY35dEAIFYvOhtD2cztVuq15qw1",
        },
        {
            "titulo": "Video 2: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Cateto opuesto, cateto adyacente e hipotenusa | Ubicar correctamente.",
            "url": "https://www.youtube.com/watch?v=FUMlQtJfrHo&list=PLeySRPnY35dEAIFYvOhtD2cztVuq15qw1&index=2",
        },
        # --- NUEVOS VIDEOS: NÚMEROS Y OPERACIONES (3 al 10) ---
        {
            "titulo": "Video 3: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Suma, resta y multiplicación.",
            "url": "https://www.youtube.com/watch?v=VvvtknaN0j0&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA&index=3",
        },
        {
            "titulo": "Video 4: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Eliminar signos de agrupación | Ejemplo 1.",
            "url": "https://www.youtube.com/watch?v=ASvBBYxDhE0&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA&index=4",
        },
        {
            "titulo": "Video 5: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Eliminar signos de agrupación | Ejemplo 2.",
            "url": "https://www.youtube.com/watch?v=WS5rtL9tTpU&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA&index=5",
        },
        {
            "titulo": "Video 6: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Eliminar signos de agrupación | Ejemplo 3 | Suma, resta y mutiplicación.",
            "url": "https://www.youtube.com/watch?v=Ld4gka7goSg&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA&index=7",
        },
        {
            "titulo": "Video 7: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Eliminar signos de agrupación | Ejemplo 4 | Suma, resta y multiplicación.",
            "url": "https://www.youtube.com/watch?v=jdqwzCL_PG0&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA&index=7",
        },
        {
            "titulo": "Video 8: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Operaciones combinadas con números enteros | Suma, resta, multiplicación, división y paréntesis.",
            "url": "https://www.youtube.com/watch?v=UbqjPCAjUfg&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA&index=8",
        },
        {
            "titulo": "Video 9: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Operaciones combinadas | suma, resta, multiplicación, división, potenciación, radicación | Ejemplo 2.",
            "url": "https://www.youtube.com/watch?v=1aJTsc11Czs&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA&index=9",
        },
        {
            "titulo": "Video 10: Números y operaciones",
            "tema": "numeros",
            "tipo": "Video",
            "descripcion": "Operaciones combinadas | suma, resta, multiplicación, división, potenciación, radicación | Ejemplo 3.",
            "url": "https://www.youtube.com/watch?v=29Z-cRvi7RQ&list=PLeySRPnY35dF1DoKO_5VyboxzdT4UyyPA&index=10",
        },
        # --- NUEVOS VIDEOS: ÁLGEBRA (3 al 10) ---
        {
            "titulo": "Video 3: Álgebra",
            "tema": "algebra",
            "tipo": "Video",
            "descripcion": "Términos semejantes.",
            "url": "https://www.youtube.com/watch?v=_0vaN7XMUsg&list=PLeySRPnY35dGSJYCRn7tD1mVatw3MrdIm&index=3",
        },
        {
            "titulo": "Video 4: Álgebra",
            "tema": "algebra",
            "tipo": "Video",
            "descripcion": "Reducción de términos semejantes.",
            "url": "https://www.youtube.com/watch?v=5yFP-mMCfB8&list=PLeySRPnY35dGSJYCRn7tD1mVatw3MrdIm&index=4",
        },
        {
            "titulo": "Video 5: Álgebra",
            "tema": "algebra",
            "tipo": "Video",
            "descripcion": "Tipos de polinomios | Clasificación de polinomios algebraicos.",
            "url": "https://www.youtube.com/watch?v=oV6H48U4SHI&list=PLeySRPnY35dGSJYCRn7tD1mVatw3MrdIm&index=5",
        },
        {
            "titulo": "Video 6: Álgebra",
            "tema": "algebra",
            "tipo": "Video",
            "descripcion": "Grado de un polinomio.",
            "url": "https://www.youtube.com/watch?v=TuVxm7tbu6s&list=PLeySRPnY35dGSJYCRn7tD1mVatw3MrdIm&index=6",
        },
        {
            "titulo": "Video 7: Álgebra",
            "tema": "algebra",
            "tipo": "Video",
            "descripcion": "Clasificación de los polinomios.",
            "url": "https://www.youtube.com/watch?v=vvIYwabU1lw&list=PLeySRPnY35dGSJYCRn7tD1mVatw3MrdIm&index=7",
        },
        {
            "titulo": "Video 8: Álgebra",
            "tema": "algebra",
            "tipo": "Video",
            "descripcion": "Grado de un polinomio.",
            "url": "https://www.youtube.com/watch?v=cJLC1SAif6k&list=PLeySRPnY35dGSJYCRn7tD1mVatw3MrdIm&index=8",
        },
       
        # --- NUEVOS VIDEOS: FUNCIONES (3 al 10) ---
        {
            "titulo": "Video 3: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "Evaluar funciones | Ejemplo 1.",
            "url": "https://www.youtube.com/watch?v=tZ8AYOOB9G4&list=PLeySRPnY35dGfEuNGbQmymhiQF4oTUIMb&index=3",
        },
        {
            "titulo": "Video 4: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "Evaluar funciones | Ejemplo 2.",
            "url": "https://www.youtube.com/watch?v=ulRV6rTSdt0&list=PLeySRPnY35dGfEuNGbQmymhiQF4oTUIMb&index=4",
        },
        {
            "titulo": "Video 5: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "Evaluar funciones | Ejemplo 3.",
            "url": "https://www.youtube.com/watch?v=8soQJtYlPis&list=PLeySRPnY35dGfEuNGbQmymhiQF4oTUIMb&index=5",
        },
        {
            "titulo": "Video 6: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "Representación de funciones.",
            "url": "https://www.youtube.com/watch?v=A7OrJ8IlIeE&list=PLeySRPnY35dGfEuNGbQmymhiQF4oTUIMb&index=6",
        },
        {
            "titulo": "Video 7: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "Dominio y rango de una función.",
            "url": "https://www.youtube.com/watch?v=H40lcwlgPMk&list=PLeySRPnY35dGfEuNGbQmymhiQF4oTUIMb&index=7",
        },
        {
            "titulo": "Video 8: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "Gráfica de la función lineal | Ejemplo 1.",
            "url": "https://www.youtube.com/watch?v=AoZpzAoC1Qg&list=PLeySRPnY35dGfEuNGbQmymhiQF4oTUIMb&index=8",
        },
        {
            "titulo": "Video 9: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "Gráfica de la función lineal | Ejemplo 2.",
            "url": "https://www.youtube.com/watch?v=jVx1jBJDEpY&list=PLeySRPnY35dGfEuNGbQmymhiQF4oTUIMb&index=9",
        },
        {
            "titulo": "Video 10: Funciones",
            "tema": "funciones",
            "tipo": "Video",
            "descripcion": "Gráfica de la función lineal | Ejemplo 3.",
            "url": "https://www.youtube.com/watch?v=4cP5oXkv7BM&list=PLeySRPnY35dGfEuNGbQmymhiQF4oTUIMb&index=10",
        },
        # --- NUEVOS VIDEOS: GEOMETRÍA (3 al 10) ---
        {
            "titulo": "Video 3: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "ÁNGULOS entre PARALELAS y SECANTES 📐 Correspondientes, Alternos, Colaterales y Opuestos por Vértice.",
            "url": "https://www.youtube.com/watch?v=5_ky4mWpSA4&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi&index=3",
        },
        {
            "titulo": "Video 4: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "ÁNGULOS entre PARALELAS y SECANTES 📐 Ejercicio Práctico.",
            "url": "https://www.youtube.com/watch?v=FF98aSvEY6k&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi&index=4",
        },
        {
            "titulo": "Video 5: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "Calcular el Área del CUADRADO y el Área del RECTÁNGULO ⏹ Figuras Planas.",
            "url": "https://www.youtube.com/watch?v=Ot-9ANd0CFQ&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi&index=5",
        },
        {
            "titulo": "Video 6: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "Calcular el Área del TRIÁNGULO y Fórmula de Herón 🔺 Figuras Planas.",
            "url": "https://www.youtube.com/watch?v=kN96aR_9b6g&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi&index=6",
        },
        {
            "titulo": "Video 7: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "Calcular la BASE de un TRIÁNGULO conociendo Área y Altura 🔺 Ejercicios de Geometría.",
            "url": "https://www.youtube.com/watch?v=bYLIpHBXKRA&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi&index=7",
        },
        {
            "titulo": "Video 8: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "Calcular el ÁREA de un TRAPECIO 🔶 Figuras Planas.",
            "url": "https://www.youtube.com/watch?v=01oj5VA56Zk&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi&index=8",
        },
        {
            "titulo": "Video 9: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "ÁREA del ROMBO y ROMBOIDE 🔶 Figuras Planas.",
            "url": "https://www.youtube.com/watch?v=uDTFbMQeVK8&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi&index=9",
        },
        {
            "titulo": "Video 10: Geometría",
            "tema": "geometria",
            "tipo": "Video",
            "descripcion": "ÁREA de POLÍGONOS REGULARES 📝 Figuras Planas.",
            "url": "https://www.youtube.com/watch?v=6Rk2POphvFY&list=PLiWRH3aE37VK5Tauc9rRKCTJUMUQmh5Yi&index=10",
        },
        # --- NUEVOS VIDEOS: TRIGONOMETRÍA (3 al 10) ---
        {
            "titulo": "Video 3: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Trucos para memorizar las razones trigonométricas.",
            "url": "https://www.youtube.com/watch?v=W4DpA-puWgw&list=PLeySRPnY35dEAIFYvOhtD2cztVuq15qw1&index=3",
        },
        {
            "titulo": "Video 4: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Razones trigonométricas de un ángulo | Ejemplo 1.",
            "url": "https://www.youtube.com/watch?v=Eh2SXkZR9BY&list=PLeySRPnY35dEAIFYvOhtD2cztVuq15qw1&index=4",
        },
        {
            "titulo": "Video 5: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Razones trigonométricas de un ángulo | Ejemplo 2.",
            "url": "https://www.youtube.com/watch?v=Qx8n_-Te-wk&list=PLeySRPnY35dEAIFYvOhtD2cztVuq15qw1&index=5",
        },
        {
            "titulo": "Video 6: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Trigonometría uso correcto de la calculadora | Fx 82, 95, 570 MS y similares.",
            "url": "https://www.youtube.com/watch?v=4mpKZMrFauw&list=PLeySRPnY35dEAIFYvOhtD2cztVuq15qw1&index=6",
        },
        {
            "titulo": "Video 7: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Trigonometría uso correcto de la calculadora fx 82, 85, 95, 350, 570, 911 SL o LA PLUS.",
            "url": "https://www.youtube.com/watch?v=dB24euc2-jE&list=PLeySRPnY35dEAIFYvOhtD2cztVuq15qw1&index=7",
        },
        {
            "titulo": "Video 8: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Trigonometría uso correcto de la calculadora | Casio Classwiz 991 LAX y similares.",
            "url": "https://www.youtube.com/watch?v=hngTp74B48A&list=PLeySRPnY35dEAIFYvOhtD2cztVuq15qw1&index=8",
        },
        {
            "titulo": "Video 9: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Razones trigonométricas | Hallar un LADO | Ejemplo 1.",
            "url": "https://www.youtube.com/watch?v=_IWs9s3XdOA&list=PLeySRPnY35dEAIFYvOhtD2cztVuq15qw1&index=9",
        },
        {
            "titulo": "Video 10: Trigonometría",
            "tema": "trigonometria",
            "tipo": "Video",
            "descripcion": "Razones trigonométricas | Hallar un LADO | Ejemplo 2.",
            "url": "https://www.youtube.com/watch?v=_wTeoKAwtHo&list=PLeySRPnY35dEAIFYvOhtD2cztVuq15qw1&index=10",
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