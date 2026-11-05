# Fusión Backend-TB + Frontend-MK

## Estructura resultante
- `core/`        (TB) modelos, migraciones, admin, comando `importar_ejercicios` y `core/data/ejercicios_diagnostico_35.csv`
- `diagnostico/` (MK) interfaz de la evaluación; ahora lee preguntas de la BD y corrige en el servidor
- `recursos/`    (MK, antes vacía) ruta de estudio: temas de más débil a más fuerte + retroalimentación + enlaces
- `sitio/`       un solo proyecto (ambos ramas tenían uno): `core` agregado a INSTALLED_APPS, URLs unificadas

## Primer arranque
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py importar_ejercicios      # carga los 35 ejercicios (idempotente)
    python manage.py createsuperuser          # para cargar Recursos en /admin/
    python manage.py runserver
Luego abrir http://127.0.0.1:8000/ 
