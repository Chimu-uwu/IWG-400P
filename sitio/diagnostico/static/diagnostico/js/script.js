
// ===========================================
// 1. BUSCAR LOS ELEMENTOS DEL HTML
// ===========================================

const contenedor = document.getElementById(
    "evaluacion-interactiva"
);

// Solo ejecutamos el código en la página
// que contiene una evaluación.
if (contenedor) {

    // Leemos la asignatura enviada por Django.
    const asignatura = contenedor.dataset.asignatura;

    // ===========================================
    // 2. PREGUNTAS DE DEMOSTRACIÓN
    // ===========================================

    const preguntasMatematicas = [
        {
            enunciado: "¿Cuánto es (3 + 5) × 2 - 4?",
            alternativas: ["10", "12", "14", "16"]
        },
        {
            enunciado: "¿Cuál es el valor de x si 2x + 6 = 18?",
            alternativas: ["4", "5", "6", "8"]
        },
        {
            enunciado: "¿Cuánto es 2 elevado a 4?",
            alternativas: ["8", "12", "16", "32"]
        }
    ];

    const preguntasFisica = [
        {
            enunciado: "¿Cuál es la unidad de fuerza en el Sistema Internacional?",
            alternativas: [
                "Joule",
                "Newton",
                "Watt",
                "Pascal"
            ]
        },
        {
            enunciado: "Un objeto recorre 100 metros en 20 segundos. ¿Cuál es su rapidez media?",
            alternativas: [
                "2 m/s",
                "5 m/s",
                "10 m/s",
                "20 m/s"
            ]
        },
        {
            enunciado: "¿Cuál de las siguientes magnitudes es vectorial?",
            alternativas: [
                "Masa",
                "Temperatura",
                "Velocidad",
                "Tiempo"
            ]
        }
    ];

    // Seleccionamos las preguntas correspondientes.
    const preguntas = asignatura === "fisica"
        ? preguntasFisica
        : preguntasMatematicas;

    // ===========================================
    // 3. VARIABLES DE CONTROL
    // ===========================================

    let preguntaActual = 0;

    // Guardaremos aquí las respuestas seleccionadas.
    const respuestas = Array(preguntas.length).fill(null);

    // Tiempo de demostración: 40 minutos.
    let tiempoRestante = 40 * 60;

    let evaluacionFinalizada = false;

    // ===========================================
    // 4. REFERENCIAS A ELEMENTOS VISUALES
    // ===========================================

    const numeroPregunta = document.getElementById(
        "numero-pregunta"
    );

    const enunciado = document.getElementById(
        "enunciado"
    );

    const alternativas = document.getElementById(
        "alternativas"
    );

    const progreso = document.getElementById(
        "progreso-relleno"
    );

    const btnAnterior = document.getElementById(
        "btn-anterior"
    );

    const btnSiguiente = document.getElementById(
        "btn-siguiente"
    );

    const temporizador = document.getElementById(
        "temporizador"
    );

    const mensajeFinal = document.getElementById(
        "mensaje-final"
    );

    // ===========================================
    // 5. MOSTRAR UNA PREGUNTA
    // ===========================================

    function mostrarPregunta() {

        const pregunta = preguntas[preguntaActual];

        numeroPregunta.textContent =
            `Pregunta ${preguntaActual + 1} de ${preguntas.length}`;

        enunciado.textContent = pregunta.enunciado;

        // Limpiamos las alternativas anteriores.
        alternativas.innerHTML = "";

        pregunta.alternativas.forEach((texto, indice) => {

            // Creamos una etiqueta HTML.
            const etiqueta = document.createElement("label");
            etiqueta.className = "alternativa";

            // Creamos un botón de selección.
            const radio = document.createElement("input");
            radio.type = "radio";
            radio.name = "respuesta";
            radio.value = indice;

            // Comprobamos si ya fue seleccionada.
            const seleccionada =
                respuestas[preguntaActual] === indice;

            radio.checked = seleccionada;

            if (seleccionada) {
                etiqueta.classList.add("seleccionada");
            }

            // Guardamos la respuesta al seleccionarla.
            radio.addEventListener("change", () => {
                respuestas[preguntaActual] = indice;
                mostrarPregunta();
            });

            const letra = String.fromCharCode(65 + indice);

            const textoAlternativa =
                document.createElement("span");

            textoAlternativa.textContent =
                `${letra}) ${texto}`;

            etiqueta.appendChild(radio);
            etiqueta.appendChild(textoAlternativa);

            alternativas.appendChild(etiqueta);
        });

        // Calculamos el avance de navegación.
        const porcentaje =
            ((preguntaActual + 1) / preguntas.length) * 100;

        progreso.style.width = `${porcentaje}%`;

        // Desactivamos Anterior en la primera pregunta.
        btnAnterior.disabled = preguntaActual === 0;

        // Cambiamos el texto del último botón.
        btnSiguiente.textContent =
            preguntaActual === preguntas.length - 1
                ? "Finalizar demostración"
                : "Siguiente →";
    }

    // ===========================================
    // 6. NAVEGACIÓN ENTRE PREGUNTAS
    // ===========================================

    btnAnterior.addEventListener("click", () => {
        if (preguntaActual > 0) {
            preguntaActual--;
            mostrarPregunta();
        }
    });

    btnSiguiente.addEventListener("click", () => {

        if (preguntaActual < preguntas.length - 1) {
            preguntaActual++;
            mostrarPregunta();
        } else {
            finalizarEvaluacion();
        }
    });

    // ===========================================
    // 7. TEMPORIZADOR
    // ===========================================

    function actualizarTemporizador() {

        const minutos = Math.floor(tiempoRestante / 60);
        const segundos = tiempoRestante % 60;

        temporizador.textContent =
            `${String(minutos).padStart(2, "0")}:` +
            `${String(segundos).padStart(2, "0")}`;
    }

    const intervalo = setInterval(() => {

        if (evaluacionFinalizada) {
            clearInterval(intervalo);
            return;
        }

        tiempoRestante--;
        actualizarTemporizador();

        if (tiempoRestante <= 0) {
            finalizarEvaluacion();
        }

    }, 1000);

    // ===========================================
    // 8. FINALIZAR LA DEMOSTRACIÓN
    // ===========================================

    function finalizarEvaluacion() {

        if (evaluacionFinalizada) return;

        evaluacionFinalizada = true;
        clearInterval(intervalo);

        numeroPregunta.hidden = true;
        temporizador.hidden = true;

        enunciado.hidden = true;
        alternativas.hidden = true;

        progreso.style.width = "100%";

        btnAnterior.hidden = true;
        btnSiguiente.hidden = true;

        mensajeFinal.hidden = false;
    }

    // ===========================================
    // 9. INICIAR LA INTERFAZ
    // ===========================================

    actualizarTemporizador();
    mostrarPregunta();
}
