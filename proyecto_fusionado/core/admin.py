from django.contrib import admin
from .models import Estudiante, EvaluacionDiagnostica, Resultado, Recurso, Ejercicio

admin.site.register(Estudiante)
admin.site.register(EvaluacionDiagnostica)
admin.site.register(Resultado)


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'materia', 'tema', 'nivel_dificultad', 'enlace')
    list_filter = ('materia', 'tipo', 'nivel_dificultad')
    search_fields = ('titulo', 'tema')


@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'materia', 'tema', 'nivel_dificultad', 'respuesta_correcta', 'fuente')
    list_filter = ('materia', 'tema', 'nivel_dificultad')
    search_fields = ('codigo', 'enunciado')
