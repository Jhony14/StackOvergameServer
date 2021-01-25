from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class ControladorUsuario(BaseUserManager):
    def create_user(self, Correo, password, **extra_fields):
        if not Correo:
            raise ValueError(_('The Correo must be set'))
        Correo = self.normalize_email(Correo)
        user = self.model(Correo=Correo, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, Correo, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(Correo, password, **extra_fields)
