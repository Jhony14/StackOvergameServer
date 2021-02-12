from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import ControladorUsuario


# Create your models here.


class Tipousuario(models.Model):
    TipousuarioId = models.AutoField(primary_key=True)
    TipousuarioNombre = models.CharField(max_length=50)


class Pruebas(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/')


class Usuario(AbstractBaseUser, PermissionsMixin):
    Correo = models.EmailField(_('correo address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    FechaCreaccion = models.DateTimeField(default=timezone.now)
    Nombre = models.CharField(max_length=100)
    Apellido1 = models.CharField(max_length=100)
    Apellido2 = models.CharField(max_length=100)
    Imagenperfil = models.ImageField(upload_to='UserProfile/')

    USERNAME_FIELD = 'Correo'
    REQUIRED_FIELDS = []

    objects = ControladorUsuario()

    def __str__(self):
        return self.Correo


class Valoracionpost(models.Model):
    ValoracionpostId = models.AutoField(primary_key=True)
    ValoracionpostNumero = models.SmallIntegerField()
    ValoracionpostUsuarioId = models.IntegerField()


class Post(models.Model):
    PostId = models.AutoField(primary_key=True)
    PostTitulo = models.CharField(max_length=255)
    PostContenido = models.TextField()
    PostFechaPublicacion = models.DateField(default=timezone.now)
    PostEstado = models.BooleanField()
    PostUsuarioId = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    PostValoracionpostId = models.ForeignKey(
        Valoracionpost, on_delete=models.CASCADE, null=True)


class Imagenespost(models.Model):
    ImagenespostId = models.AutoField(primary_key=True)
    ImagenespostNombre = models.CharField(max_length=255)
    ImagenespostTipo = models.CharField(max_length=50)
    # para almacenar la ruta que se guardara en disco
    ImagenespostArchivo = models.CharField(max_length=255)
    ImagenespostPostId = models.IntegerField(null=True)


class Comentarios(models.Model):
    ComentariosId = models.AutoField(primary_key=True)
    ComentariosContenido = models.TextField()
    ComentariosFechaComentario = models.DateField(default=timezone.now)
    ComentariosEstado = models.BooleanField()
    ComentariosUsuarioId = models.IntegerField()
    ComentariosPostId = models.IntegerField()
    ComentariosValoracioncomentariosId = models.IntegerField()


class Imagenescomentarios(models.Model):
    ImagenescomentariosId = models.AutoField(primary_key=True)
    ImagenescomentariosNombre = models.CharField(max_length=255)
    ImagenescomentariosTipo = models.CharField(max_length=50)
    # para almacenar la ruta que se guardara en disco
    ImagenescomentariosArchivo = models.CharField(max_length=255)
    ImagenescomentariosComentariosId = models.IntegerField(null=True)


class Valoracioncomentarios(models.Model):
    ValoraciValoracioncomentariosIdonId = models.AutoField(primary_key=True)
    ValoracioncomentariosNumero = models.SmallIntegerField()
    ValoracioncomentariosUsuarioId = models.IntegerField()
