from django.shortcuts import render

# Create your views here.

def vista_diagnostico(request):
    return render(request, 'diagnostico/evaluacion.html')
