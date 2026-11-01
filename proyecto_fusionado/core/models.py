#modelos para interacturar con la base de datos

from django.db import models
from django.contrib.auth.models import User #esto es para la interacción de usuarios


class Estudiante(models.Model):
    # Conectamos con el sistema de usuarios de Django (maneja correo, nombre y contraseña)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    id_estudiante = models.CharField(max_length=20, unique=True, verbose_name="Rol USM")

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name} - {self.id_estudiante}"

#interación con las evaluaciones
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


#almacerá los resultados de la evaluación diagnóstica
class Resultado(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(EvaluacionDiagnostica, on_delete=models.CASCADE)
    puntaje_obtenido = models.FloatField()
    fecha_rendicion = models.DateTimeField(auto_now_add=True)
    resultados_detallados = models.TextField(help_text="Resumen de los vacíos conceptuales detectados")

    def __str__(self):
        return f"Resultado de {self.estudiante.usuario.username} - {self.evaluacion.titulo}"


# 4.
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
    materia = models.CharField(max_length=3)  # CAL, ALG, FIS
    # NUEVO (fusión): permite asociar el recurso al tema donde el estudiante falló.
    tema = models.CharField(max_length=100, blank=True, default='',
                            help_text="Mismo nombre que el tema del ejercicio. Vacío = sirve para toda la materia.")
    nivel_dificultad = models.IntegerField(choices=NIVELES)
    enlace = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - Nivel {self.nivel_dificultad}"

#tabla para almacenar los ejercicios
class Ejercicio(models.Model):
    LETRAS = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]

    #id y enonciados
    codigo = models.CharField(max_length=10, unique=True, null=True, blank=True) #este es el id de la pregunta
    tema = models.CharField(max_length=100, blank=True, default='')
    materia = models.CharField(max_length=3)  # CAL, ALG, FIS
    enunciado = models.TextField()
    
   #alternativas de cada pregunta
    alt_a = models.CharField(max_length=200, blank=True, default='')
    alt_b = models.CharField(max_length=200, blank=True, default='')
    alt_c = models.CharField(max_length=200, blank=True, default='')
    alt_d = models.CharField(max_length=200, blank=True, default='')
    respuesta_correcta = models.CharField(max_length=1, choices=LETRAS)
    
    #dificultad de las preguntas
    nivel_dificultad = models.IntegerField(choices=Recurso.NIVELES)
    
    #de donde se ha sacado y consejo para cada respuesta
    fuente = models.CharField(max_length=100, blank=True, default='')
    retroalimentacion = models.TextField(help_text="Explicación si el estudiante se equivoca")

    class Meta:
        ordering = ['codigo', 'id']

    @property
    def alternativas(self):
        return [self.alt_a, self.alt_b, self.alt_c, self.alt_d]

    def __str__(self):
        return f"{self.codigo or self.id} - {self.tema} (dificultad {self.nivel_dificultad})"
