"""
URL configuration for sitio project.

Fusión Backend-TB + Frontend-MK:
  /                  -> redirige a la página de inicio del diagnóstico
  /diagnostico/...   -> evaluación (Frontend-MK)
  /recursos/...      -> ruta de estudio con enlaces a recursos
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='inicio', permanent=False)),
    path('diagnostico/', include('diagnostico.urls')),
    path('recursos/', include('recursos.urls')),
]
