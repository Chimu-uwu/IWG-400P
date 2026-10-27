from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Recurso, Estudiante

# Vista de la página principal (la que ya tenías)
def inicio(request):
    return render(request, 'core/inicio.html')

# Vista de tu cápsula de materia (la nueva)

# @login_required
def portal_materia(request):
    # estudiante_actual = Estudiante.objects.get(usuario=request.user)
    
    # Mantenemos un filtro fijo por ahora para probar
    recursos_recomendados = Recurso.objects.filter(nivel_dificultad=2)
    
    return render(request, 'core/portal.html', {
        'recursos': recursos_recomendados
    })
    
    #