import csv
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from core.models import Ejercicio

CSV_POR_DEFECTO = Path(__file__).resolve().parents[2] / 'data' / 'ejercicios_diagnostico_35.csv'

COLUMNAS = {'id', 'tema', 'materia', 'enunciado', 'alt_a', 'alt_b', 'alt_c', 'alt_d',
            'correcta', 'dificultad', 'retroalimentacion', 'fuente'}


class Command(BaseCommand):
    help = "Importa el banco de ejercicios del diagnóstico desde un CSV. Es idempotente: reimportar actualiza, no duplica."

    def add_arguments(self, parser):
        parser.add_argument('csv', nargs='?', default=str(CSV_POR_DEFECTO),
                            help="Ruta del CSV (por defecto core/data/ejercicios_diagnostico_35.csv)")

    @transaction.atomic
    def handle(self, *args, **opts):
        ruta = Path(opts['csv'])
        if not ruta.exists():
            raise CommandError(f"No existe el archivo: {ruta}")

        # utf-8-sig tolera el BOM que agrega Excel
        with ruta.open(newline='', encoding='utf-8-sig') as f:
            lector = csv.DictReader(f)
            faltan = COLUMNAS - set(lector.fieldnames or [])
            if faltan:
                raise CommandError(f"Faltan columnas en el CSV: {', '.join(sorted(faltan))}")

            creados = actualizados = 0
            for n, fila in enumerate(lector, start=2):  # fila 1 = encabezado
                letra = fila['correcta'].strip().upper()
                if letra not in 'ABCD' or len(letra) != 1:
                    raise CommandError(f"Línea {n}: 'correcta' debe ser A, B, C o D (llegó {fila['correcta']!r})")
                try:
                    dificultad = int(fila['dificultad'])
                except ValueError:
                    raise CommandError(f"Línea {n}: 'dificultad' no es un número")
                if dificultad not in (1, 2, 3):
                    raise CommandError(f"Línea {n}: 'dificultad' debe ser 1, 2 o 3")

                _, creado = Ejercicio.objects.update_or_create(
                    codigo=fila['id'].strip(),
                    defaults=dict(
                        tema=fila['tema'].strip(),
                        materia=fila['materia'].strip().upper(),
                        enunciado=fila['enunciado'].strip(),
                        alt_a=fila['alt_a'].strip(),
                        alt_b=fila['alt_b'].strip(),
                        alt_c=fila['alt_c'].strip(),
                        alt_d=fila['alt_d'].strip(),
                        respuesta_correcta=letra,
                        nivel_dificultad=dificultad,
                        retroalimentacion=fila['retroalimentacion'].strip(),
                        fuente=fila['fuente'].strip(),
                    ),
                )
                creados += creado
                actualizados += not creado

        self.stdout.write(self.style.SUCCESS(
            f"Importación lista: {creados} creados, {actualizados} actualizados."))
