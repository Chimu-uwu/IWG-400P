document.addEventListener("DOMContentLoaded", function () {
    // Duración de la evaluación: 40 minutos
    const DURACION_INICIAL = 40 * 60;

    let tiempoRestante = DURACION_INICIAL;
    let temporizador = null;
    let evaluacionTerminada = false;

    const contador = document.getElementById("countdown");

    // Comprueba que el contador exista en el HTML
    if (!contador) {
        console.error("No se encontró el elemento #countdown.");
        return;
    }

    // Actualiza el texto con formato MM:SS
    function actualizarContador() {
        const minutos = Math.floor(tiempoRestante / 60);
        const segundos = tiempoRestante % 60;

        contador.textContent =
            String(minutos).padStart(2, "0") + ":" +
            String(segundos).padStart(2, "0");
    }

    // Finaliza la evaluación cuando el tiempo se agota
    function finalizarPorTiempo() {
        clearInterval(temporizador);
        temporizador = null;
        evaluacionTerminada = true;

        contador.textContent = "00:00";

        alert("¡Se acabó el tiempo! La evaluación ha finalizado.");
    }

    // Ejecuta una actualización por segundo
    function iniciarContador() {
        actualizarContador();

        temporizador = setInterval(function () {
            if (evaluacionTerminada) {
                clearInterval(temporizador);
                return;
            }

            tiempoRestante--;

            if (tiempoRestante <= 0) {
                tiempoRestante = 0;
                actualizarContador();
                finalizarPorTiempo();
                return;
            }

            actualizarContador();
        }, 1000);
    }

    // Inicia la cuenta regresiva
    iniciarContador();
});