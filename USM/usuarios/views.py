
from django.shortcuts import render,redirect
from .forms import RegistroForm, LoginForm
from django.contrib.auth import login,logout 
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import IntegrityError, transaction


def vista_login(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST' :
        form = LoginForm(request, data=request.POST)
        if form.is_valid() :
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')
      
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})


def vista_registro(request):

    if request.method == 'POST':
        form = RegistroForm(request.POST)

        print("Se recibió un POST de registro")

        if form.is_valid():
            print("Formulario válido")

            try:
                # Intenta guardar el usuario en la base de datos
                with transaction.atomic():
                    usuario = form.save()

            except IntegrityError:
                # Si otro usuario registró el mismo correo
                # antes de que terminara esta petición
                form.add_error("username","Este correo electrónico ya está registrado.")
                print("Error: correo electrónico duplicado")

            else:
                # El usuario se creó correctamente
                print("Usuario guardado:", usuario.username)
                login(request, usuario)
                return redirect('inicio')
        else:
            print("Errores del formulario:", form.errors)

    else:
        form = RegistroForm()
    return render(request,'usuarios/registro.html',{'form': form})

@login_required
@require_POST

def vista_logout(request):
    logout(request)
    return redirect('login')

def vista_inicio(request):
    return render(request, 'diagnostico/inicio.html')
