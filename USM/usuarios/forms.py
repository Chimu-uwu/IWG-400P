
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)
from django.contrib.auth.models import User


# ==========================================
# 1. FORMULARIO DE REGISTRO
# ==========================================

class RegistroForm(UserCreationForm):

    # Nombre que ingresará el estudiante
    nombre = forms.CharField(
        label="Nombre completo",
        max_length=150
    )

    # Utilizamos username para guardar el correo
    username = forms.EmailField(
        label="Correo electrónico",
        max_length=150
    )

    class Meta:
        model = User
        fields = [
            "nombre",
            "username",
            "password1",
            "password2"
        ]

    # Normalizamos el correo y comprobamos
    # que todavía no exista una cuenta con él.
    def clean_username(self):

        correo = self.cleaned_data["username"]
        correo = correo.strip().lower()

        if User.objects.filter(
            username__iexact=correo
        ).exists():
            raise forms.ValidationError(
                "Ya existe una cuenta con este correo."
            )

        return correo

    # Guardamos los datos adicionales
    def save(self, commit=True):

        usuario = super().save(commit=False)

        usuario.email = self.cleaned_data["username"]
        usuario.first_name = self.cleaned_data["nombre"]

        if commit:
            usuario.save()

        return usuario


# ==========================================
# 2. FORMULARIO DE INICIO DE SESIÓN
# ==========================================

class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        label="Correo electrónico",
        max_length=150
    )
