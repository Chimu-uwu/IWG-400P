import csv

from diagnostico.models import Ejercicio

with open("ejercicios_diagnostico_35.csv", encoding="utf-8") as archivo:

    lector = csv.DictReader(archivo)

    for fila in lector:

        Ejercicio.objects.create(
            materia=fila["materia"],
            nivel_dificultad=int(fila["dificultad"]),
            enunciado=fila["enunciado"],
            opcion_A=fila["alt_a"],
            opcion_B=fila["alt_b"],
            opcion_C=fila["alt_c"],
            opcion_D=fila["alt_d"],
            respuesta_correcta=fila["correcta"],
            retroalimentacion=fila["retroalimentacion"]
        )

print("Carga completada")