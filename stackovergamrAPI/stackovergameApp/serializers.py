from rest_framework import serializers
from stackovergameApp.models import Pruebas, Tipousuario, Usuario, Post, Comentarios, Imagenespost, Imagenescomentarios, Valoracionpost, Valoracioncomentarios


class TipousuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipousuario
        fields = ('TipousuarioId', 'TipousuarioNombre')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class PruebasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pruebas
        fields = '__all__'


class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'Nombre', 'Apellido1',
                  'Apellido2', 'Correo', 'Imagenperfil')


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
