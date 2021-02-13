from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


from stackovergameApp.models import Pruebas, Tipousuario, Usuario, Post, Comentarios, Imagenespost, Imagenescomentarios, Valoracionpost, Valoracioncomentarios


class UserSignUpSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )

    photo = serializers.ImageField(
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png'])],
        required=False
    )

    extract = serializers.CharField(max_length=1000, required=False)

    city = serializers.CharField(max_length=250, required=False)

    country = serializers.CharField(max_length=250, required=False)

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Debes introducir un número con el siguiente formato: +999999999. El límite son de 15 dígitos."
    )
    phone = serializers.CharField(validators=[phone_regex], required=False)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)

        image = None
        if 'photo' in data:
            image = data['photo']

        if image:
            if image.size > (512 * 1024):
                raise serializers.ValidationError(
                    f"La imagen es demasiado grande, el peso máximo permitido es de 512KB y el tamaño enviado es de {round(image.size / 1024)}KB")

        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = Usuario.objects.create_user(**data)
        return user


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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('Correo', 'password', 'Nombre',
                  'Apellido1', 'Apellido2', 'Imagenperfil')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('PostId', 'PostTitulo', 'PostContenido', 'PostFechaPublicacion',
                  'PostEstado', 'PostUsuarioId', 'PostValoracionpostId')


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('PostId', 'PostTitulo', 'PostFechaPublicacion')


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
