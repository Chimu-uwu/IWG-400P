
from django.urls import path
from . import views

urlpatterns = [

    # Página de inicio
    path('',views.vista_inicio,name='inicio'),

    # Selección de evaluaciones
    path('evaluacion/',views.vista_diagnostico,name='evaluacion'),

    # Instrucciones de cada asignatura
    path('instrucciones/<str:asignatura>/',views.vista_instrucciones,name='instrucciones'),
    
    path('preguntas/<str:asignatura>/',views.vista_preguntas,name='preguntas'),


]
