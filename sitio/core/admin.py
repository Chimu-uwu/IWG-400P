from django.contrib import admin
from .models import Estudiante, EvaluacionDiagnostica, Resultado, Recurso, Ejercicio

admin.site.register(Estudiante)
admin.site.register(EvaluacionDiagnostica)
admin.site.register(Resultado)
admin.site.register(Recurso)
admin.site.register(Ejercicio)

# Register your models here.
