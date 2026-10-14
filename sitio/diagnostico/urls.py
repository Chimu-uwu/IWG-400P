from django.urls import path
from . import views

urlpatterns = [
    path('evaluacion/', views.vista_diagnostico, name='evaluacion'),
]
