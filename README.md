# IWG-400P
# IWG-400P — Plataforma de Diagnóstico Académico USM

## Descripción

Proyecto desarrollado para la asignatura IWG-400P de la Universidad Técnica Federico Santa María.

La aplicación permite a los estudiantes realizar evaluaciones diagnósticas de Matemáticas, consultar sus resultados y acceder a recursos educativos personalizados según los contenidos que necesitan reforzar.

## Funcionalidades principales

- Registro e inicio de sesión de estudiantes.
- Evaluación diagnóstica de Matemáticas con 35 preguntas.
- Corrección automática de respuestas.
- Almacenamiento del historial de resultados.
- Ruta de estudio personalizada según el rendimiento por tema.
- Almacén de videos, guías y otros recursos educativos.

## Requisitos

- Python instalado.
- Git para clonar el repositorio.
- Dependencias indicadas en `requirements.txt`.

## Instalación

**1. Clonar el repositorio**

cree una carpeta y dentro de ella. En Vs code habra la carpeta junto con una temrinal y escriba git clone https://github.com/Chimu-uwu/IWG-400P.git
cd IWG-400P


**2. Crear un entorno virtual**
 use en la terminal python -m venv venv


En Windows (PowerShell), activarlo con:


.\venv\Scripts\Activate.ps1 o venv\Scripts\activate

**3. Instalar las dependencias**

con el entorno activo y dentro de la carpeta clonada ejecute pip install -r requirements.txt

**4. Entrar en la carpeta de Django**

cd USM


**5. Crear las tablas de la base de datos**

cree la tabla de datos con python manage.py migrate


**6. Cargar las preguntas y recursos educativos**

ejecute en la terminal python manage.py loaddata ejercicios_1 ejercicios_2 recursos


**7. Iniciar el servidor**

corra el servidor con python manage.py runserver


**8. Abrir la aplicación**

Ingresar en el navegador a:

http://127.0.0.1:8000/diagnostico/ , esto lo redirigira automaticamente al login 

## Instrucciones para probar la aplicación :O

1. Acceder a la plataforma y registrar una cuenta de estudiante con un correo electrónico y contraseña.
2. Iniciar sesión, si todavía no se ha iniciado automáticamente.
3. Entrar en la sección **Evaluaciones**.
4. Iniciar el diagnóstico de Matemáticas y responder las preguntas.
5. Finalizar la evaluación para obtener el puntaje.
6. Consultar la sección **Resultados** para revisar el historial.
7. Acceder a **Ruta de estudio** para revisar el desempeño por tema y los recursos recomendados.
8. Visitar **Almacén** para explorar los recursos educativos disponibles.
