from django.urls import path
from . import views

urlpatterns = [
    path('ruta/', views.ruta_estudio, name='ruta_estudio'),
]
