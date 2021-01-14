from rest_framework import serializers
from stackovergameApp.models import Tipousuario, Usuario, Post, Comentarios, Imagenespost, Imagenescomentarios, Valoracionpost, Valoracioncomentarios


class TipousuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipousuario
        fields = ('TipousuarioId', 'TipousuarioNombre')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('UsuarioId', 'UsuarioDni', 'UsuarioNombre', 'UsuarioApellido1',
                  'UsuarioApellido2', 'UsuarioLogin', 'UsuarioPassword',
                  'UsuarioEmail', 'UsuarioToken', 'UsuarioValidado',
                  'UsuarioActivo', 'UsuarioFechaCreacion', 'UsuarioProfilePicture', 'UsuarioTipousuarioId')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('PostId', 'PostTitulo', 'PostContenido', 'PostFechaPublicacion',
                  'PostEstado', 'PostUsuarioId', 'PostValoracionpostId')


class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ('ComentariosId', 'ComentariosContenido', 'ComentariosFechaComentario', 'ComentariosEstado',
                  'ComentariosUsuarioId', 'ComentariosPostId', 'ComentariosValoracioncomentariosId')


class ImagenespostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenespost
        fields = ('ImagenespostId', 'ImagenespostNombre',
                  'ImagenespostTipo', 'ImagenespostArchivo', 'ImagenespostPostId')


class ImagenescomentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenescomentarios
        fields = ('ImagenescomentariosId', 'ImagenescomentariosNombre',
                  'ImagenescomentariosTipo', 'ImagenescomentariosArchivo', 'ImagenescomentariosComentariosId')


class ValoracionpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracionpost
        fields = ('ValoracionId', 'ValoracionNumero',
                  'ValoracionpostUsuarioId')


class ValoracioncomentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracioncomentarios
        fields = ('ValoracionId', 'ValoracionNumero',
                  'ValoracionpostUsuarioId')
