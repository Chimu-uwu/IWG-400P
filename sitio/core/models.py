from django.db import models
from django.contrib.auth.models import User

# 1. Modelo Estudiante
class Estudiante(models.Model):
    # Conectamos con el sistema de usuarios de Django (maneja correo, nombre y contraseña)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    id_estudiante = models.CharField(max_length=20, unique=True, verbose_name="Rol USM")
    
    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name} - {self.id_estudiante}"

# 2. Modelo Evaluación Diagnóstica
class EvaluacionDiagnostica(models.Model):
    MATERIAS = [
        ('CAL', 'Cálculo'),
        ('ALG', 'Álgebra'),
        ('FIS', 'Física'),
    ]
    titulo = models.CharField(max_length=100)
    materia = models.CharField(max_length=3, choices=MATERIAS)
    fecha_limite = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_materia_display()})"

# 3. Modelo Resultados
class Resultado(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(EvaluacionDiagnostica, on_delete=models.CASCADE)
    puntaje_obtenido = models.FloatField()
    fecha_rendicion = models.DateTimeField(auto_now_add=True)
    resultados_detallados = models.TextField(help_text="Resumen de los vacíos conceptuales detectados")

    def __str__(self):
        return f"Resultado de {self.estudiante.usuario.username} - {self.evaluacion.titulo}"

# 4. Modelo Recursos (Para tu cápsula de materia)
class Recurso(models.Model):
    TIPOS = [
        ('VID', 'Video'),
        ('GUI', 'Guía PDF'),
        ('LIB', 'Libro recomendado'),
    ]
    NIVELES = [
        (1, 'Básico'),
        (2, 'Intermedio'),
        (3, 'Avanzado'),
    ]
    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=3, choices=TIPOS)
    materia = models.CharField(max_length=3) # CAL, ALG, FIS
    nivel_dificultad = models.IntegerField(choices=NIVELES)
    enlace = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - Nivel {self.nivel_dificultad}"

# 5. Modelo Ejercicio (Para la funcionalidad de dificultad adaptativa)
class Ejercicio(models.Model):
    enunciado = models.TextField()
    materia = models.CharField(max_length=3)
    nivel_dificultad = models.IntegerField(choices=Recurso.NIVELES)
    respuesta_correcta = models.CharField(max_length=200)
    retroalimentacion = models.TextField(help_text="Explicación si el estudiante se equivoca")

    def __str__(self):
        return f"Ejercicio {self.id} - Dificultad {self.nivel_dificultad}"

# Create your models here.
