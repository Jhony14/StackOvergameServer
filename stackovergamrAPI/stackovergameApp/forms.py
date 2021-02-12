from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

from .models import Usuario


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('Correo', 'Nombre', 'Apellido1',
                  'Apellido2', 'Imagenperfil')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('Correo',)
