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


# 4. Modelo Recursos (enlaces de la ruta de estudio)
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


# 5. Modelo Ejercicio (banco de preguntas del diagnóstico)
class Ejercicio(models.Model):
    LETRAS = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]

    # NUEVO (fusión): campos que trae el CSV ejercicios_diagnostico_35.csv
    codigo = models.CharField(max_length=10, unique=True, null=True, blank=True,
                              help_text="Identificador del CSV (ej. NUM01). Permite reimportar sin duplicar.")
    tema = models.CharField(max_length=100, blank=True, default='')
    fuente = models.CharField(max_length=100, blank=True, default='')
    alt_a = models.CharField(max_length=200, blank=True, default='')
    alt_b = models.CharField(max_length=200, blank=True, default='')
    alt_c = models.CharField(max_length=200, blank=True, default='')
    alt_d = models.CharField(max_length=200, blank=True, default='')

    enunciado = models.TextField()
    materia = models.CharField(max_length=3)  # CAL, ALG, FIS
    nivel_dificultad = models.IntegerField(choices=Recurso.NIVELES)
    # CAMBIO (fusión): ahora guarda la LETRA correcta (A-D), no el texto.
    respuesta_correcta = models.CharField(max_length=1, choices=LETRAS)
    retroalimentacion = models.TextField(help_text="Explicación si el estudiante se equivoca")

    class Meta:
        ordering = ['codigo', 'id']

    @property
    def alternativas(self):
        return [self.alt_a, self.alt_b, self.alt_c, self.alt_d]

    def __str__(self):
        return f"{self.codigo or self.id} - {self.tema} (dificultad {self.nivel_dificultad})"
