
from django.shortcuts import render


def vista_login(request):
    return render(request, 'usuarios/login.html')


def vista_registro(request):
    return render(request, 'usuarios/registro.html')
