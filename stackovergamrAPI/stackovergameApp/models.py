from django.db import models

# Create your models here.


class Tipousuario(models.Model):
    TipousuarioId = models.AutoField(primary_key=True)
    TipousuarioNombre = models.CharField(max_length=50)


class Usuario(models.Model):
    UsuarioId = models.AutoField(primary_key=True)
    UsuarioDni = models.CharField(max_length=9)
    UsuarioNombre = models.CharField(max_length=50)
    UsuarioApellido1 = models.CharField(max_length=50)
    UsuarioApellido2 = models.CharField(max_length=50)
    UsuarioLogin = models.CharField(max_length=50)
    UsuarioPassword = models.CharField(max_length=512)
    UsuarioEmail = models.CharField(max_length=255)
    UsuarioToken = models.CharField(max_length=512)
    UsuarioValidado = models.BooleanField()
    UsuarioActivo = models.BooleanField()
    UsuarioFechaCreacion = models.DateField()
    # Profile picture para almacenar la ruta que se guardara en disco
    UsuarioProfilePicture = models.CharField(max_length=255)
    UsuarioTipousuarioId = models.IntegerField()


class Post(models.Model):
    PostId = models.AutoField(primary_key=True)
    PostTitulo = models.CharField(max_length=255)
    PostContenido = models.TextField()
    PostFechaPublicacion = models.DateField()
    PostEstado = models.BooleanField()
    PostUsuarioId = models.IntegerField()
    PostValoracionpostId = models.IntegerField()


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
    ComentariosFechaComentario = models.DateField()
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


# cambiar a ValoracionpostId
class Valoracionpost(models.Model):
    ValoracionId = models.AutoField(primary_key=True)
    ValoracionNumero = models.SmallIntegerField()
    ValoracionpostUsuarioId = models.IntegerField()


# cambiar por ValoracioncomentariosId
class Valoracioncomentarios(models.Model):
    ValoracionId = models.AutoField(primary_key=True)
    ValoracionNumero = models.SmallIntegerField()
    ValoracioncomentariosUsuarioId = models.IntegerField()
