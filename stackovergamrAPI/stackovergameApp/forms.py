from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('Correo',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('Correo',)
