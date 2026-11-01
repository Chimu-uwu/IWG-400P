# NIVELACIÓN
Una aplicación web que tiene por objetivo ayudar a los estudiantes de primer año de la USM reconocer áreas débiles en contenidos básicos asociados a ramos durante la transición universitaria.

## Características principales
1. Evaluación diagnóstica: para evaluar conocimientos previos.
2. Retroalimentación: una interfaz de temas con mayor dificultad ordenados por prioridad.
3. Recursos de apoyo: contenido previamente seleccionado que puede servirle al estudiante para atacar sus debilidades.

### Instalación
1. Crear un ambiente virtual `python -m venv .venv`
2. Activar el ambiente virtual 
    - `source .venv/Scripts/activate`(bash)
    - `.\.venv\Scripts\Activate.ps1`(powershell)
3. Instalar los requirements `pip install -r requirements.txt`
5. Hacemos las migraciones `python manage.py migrate`
4. cargamos la data inicial usando las fixtures de django `python manage.py loaddata ejercicios.json`


### Modo de uso
1. En la carpeta principal del proyecto `python manage.py runserver`
2. Acceder al link proporcionado
3. Seleccionar la evaluación diagnótica 
4. Responder cuestionario y darle a finalizar
5. clickear "ver ruta de aprendizaje" 





