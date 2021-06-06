from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib import auth
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model

from stackovergameApp.models import Guide, News, Pruebas, Tipousuario, Usuario, Post, Comentarios, Imagenespost, Imagenescomentarios, Valoracionpost, Valoracioncomentarios
from stackovergameApp.serializers import GuideSerializer, NewsSerializer, PruebasSerializer, UserSerializer, UserSignUpSerializer, TipousuarioSerializer, UsuarioSerializer, UsuarioUpdateSerializer, PostAddEditSerializer, PostSerializer, PostListSerializer, ComentariosSerializer, ImagenespostSerializer, ImagenescomentariosSerializer, ValoracionpostSerializer, ValoracioncomentariosSerializer

from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def prueba(request):
    if request.method == 'GET':
        prueba = Pruebas.objects.all()
        prueba_serializar = PruebasSerializer(prueba, many=True)
        return JsonResponse(prueba_serializar.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        prueba_serializar = PruebasSerializer(data=data)
        print(prueba_serializar)
        if prueba_serializar.is_valid():
            prueba_serializar.save()
            return JsonResponse("Add ", safe=False)
        return JsonResponse("Failed", safe=False)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


@csrf_exempt
def create_user(request):
    usuario_data = JSONParser().parse(request)
    User = get_user_model()
    print(usuario_data['password'])
    user = User.objects.create_user(
        usuario_data['Correo'], usuario_data['password'], usuario_data['Nombre'], usuario_data['Apellido1'], usuario_data['Apellido2'], usuario_data['Imagenperfil'])
    return JsonResponse("create", safe=False)


@csrf_exempt
def tipousuarioApi(request, id=0):
    if request.method == 'GET':
        tipousuario = Tipousuario.objects.all()
        tipousuario_serializer = TipousuarioSerializer(tipousuario, many=True)
        return JsonResponse(tipousuario_serializer.data, safe=False)

    elif request.method == 'POST':
        tipousuario_data = JSONParser().parse(request)
        tipousuario_serializer = TipousuarioSerializer(
            data=tipousuario_data)
        if tipousuario_serializer.is_valid():
            tipousuario_serializer.save()
            return JsonResponse("Add tipo usuario", safe=False)
        return JsonResponse("Failed to add tipo usuario", safe=False)

    elif request.method == 'PUT':
        tipousuario_data = JSONParser().parse(request)
        tipousuario = Tipousuario.objects.get(
            TipousuarioId=tipousuario_data['TipousuarioId'])
        tipousuario_serializer = TipousuarioSerializer(
            tipousuario, data=tipousuario_data)
        if tipousuario_serializer.is_valid():
            tipousuario_serializer.save()
            return JsonResponse("Update Tipo usuario", safe=False)
        return JsonResponse("Failed to update tipo usuario", safe=False)

    elif request.method == 'DELETE':
        tipousuario = Tipousuario.objects.get(TipousuarioId=id)
        tipousuario.delete()
        return JsonResponse("Delete tipo usuario", safe=False)


@csrf_exempt
@action(detail=False, methods=['post'])
def signup(request):
    """User sign up."""
    serializer = UserSignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    data = UserModelSerializer(user).data
    return Response(data, status=status.HTTP_201_CREATED)


@csrf_exempt
def usuarioApi(request, id=0):

    if request.method == 'GET':
        usuario = Usuario.objects.all().filter(id=id)
        usuario_serializer = UsuarioUpdateSerializer(usuario, many=True)
        return JsonResponse(usuario_serializer.data, safe=False)

    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioUpdateSerializer(
            data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Add usuario", safe=False)
        return JsonResponse("Failed to add usuario", safe=False)

    elif request.method == 'PUT':
        usuario_data = JSONParser().parse(request)
        usuario = Usuario.objects.get(
            id=usuario_data['id'])
        usuario_serializer = UsuarioUpdateSerializer(
            usuario, data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Update usuario", safe=False)
        return JsonResponse("Failed to update usuario", safe=False)

    elif request.method == 'DELETE':
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        return JsonResponse("Delete usuario", safe=False)


@csrf_exempt
def usuarioAllApi(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuario, many=True)
        return JsonResponse(usuario_serializer.data, safe=False)


@csrf_exempt
def postListApi(request, id=0):
    if request.method == 'GET':
        post = Post.objects.all()
        post_serializer = PostListSerializer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)


@csrf_exempt
def postApi(request, id=0):
    if request.method == 'GET':
        post = Post.objects.all().filter(PostId=id)
        post_serializer = PostSerializer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)

    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostAddEditSerializer(
            data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Add post", safe=False)
        return JsonResponse("Failed to add post", safe=False)

    elif request.method == 'PUT':
        post_data = JSONParser().parse(request)
        post = Post.objects.get(
            PostId=post_data['PostId'])
        post_serializer = PostAddEditSerializer(
            post, data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Update post", safe=False)
        return JsonResponse("Failed to update post", safe=False)

    elif request.method == 'DELETE':
        post = Post.objects.get(PostId=id)
        post.delete()
        return JsonResponse("Delete post", safe=False)


@csrf_exempt
def guideListApi(request, id=0):
    if request.method == 'GET':
        guide = Guide.objects.all()
        guide_serializer = GuideSerializer(guide, many=True)
        return JsonResponse(guide_serializer.data, safe=False)


@csrf_exempt
def guideApi(request, id=0):
    if request.method == 'GET':
        guide = Guide.objects.all().filter(GuideId=id)
        guide_serializer = GuideSerializer(guide, many=True)
        return JsonResponse(guide_serializer.data, safe=False)

    elif request.method == 'POST':
        guide_data = JSONParser().parse(request)
        guide_serializer = GuideSerializer(data=guide_data)
        if guide_serializer.is_valid():
            guide_serializer.save()
            return JsonResponse("Add guide", safe=False)
        return JsonResponse("Failed to add guide", safe=False)

    elif request.method == 'PUT':
        guide_data = JSONParser().parse(request)
        guide = Guide.objects.get(GuideId=guide_data['GuideId'])
        guide_serializer = GuideSerializer(guide, data=guide_data)
        if guide_serializer.is_valid():
            guide_serializer.save()
            return JsonResponse("Update guide", safe=False)
        return JsonResponse("Failed to update guide", safe=False)

    elif request.method == 'DELETE':
        guide = Guide.objects.get(GuideId=id)
        guide.delete()
        return JsonResponse("Delete guide", safe=False)


@csrf_exempt
def newsListApi(request, id=0):
    if request.method == 'GET':
        news = News.objects.all()
        news_serializer = NewsSerializer(news, many=True)
        return JsonResponse(news_serializer.data, safe=False)


@csrf_exempt
def newsApi(request, id=0):
    if request.method == 'GET':
        news = News.objects.all().filter(NewsId=id)
        news_serializer = NewsSerializer(news, many=True)
        return JsonResponse(news_serializer.data, safe=False)

    elif request.method == 'POST':
        news_data = JSONParser().parse(request)
        news_serializer = NewsSerializer(data=news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse("Add news", safe=False)
        return JsonResponse("Failed to add news", safe=False)

    elif request.method == 'PUT':
        news_data = JSONParser().parse(request)
        news = News.objects.get(
            NewsId=news_data['NewsId'])
        news_serializer = NewsSerializer(news, data=news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse("Update news", safe=False)
        return JsonResponse("Failed to update news", safe=False)

    elif request.method == 'DELETE':
        news = News.objects.get(NewsId=id)
        news.delete()
        return JsonResponse("Delete news", safe=False)


@csrf_exempt
def comentariosApi(request, id=0):
    if request.method == 'GET':
        comentarios = Comentarios.objects.all().filter(ComentariosPostId=id)
        comentarios_serializer = ComentariosSerializer(comentarios, many=True)
        return JsonResponse(comentarios_serializer.data, safe=False)

    elif request.method == 'POST':
        comentarios_data = JSONParser().parse(request)
        comentarios_serializer = ComentariosSerializer(
            data=comentarios_data)
        if comentarios_serializer.is_valid():
            comentarios_serializer.save()
            return JsonResponse("Add comentarios", safe=False)
        return JsonResponse("Failed to add comentarios", safe=False)

    elif request.method == 'PUT':
        comentarios_data = JSONParser().parse(request)
        comentarios = Comentarios.objects.get(
            ComentariosId=comentarios_data['ComentariosId'])
        comentarios_serializer = ComentariosSerializer(
            comentarios, data=comentarios_data)
        if comentarios_serializer.is_valid():
            comentarios_serializer.save()
            return JsonResponse("Update comentarios", safe=False)
        return JsonResponse("Failed to update comentarios", safe=False)

    elif request.method == 'DELETE':
        comentarios = Comentarios.objects.get(ComentariosId=id)
        comentarios.delete()
        return JsonResponse("Delete comentarios", safe=False)


@csrf_exempt
def valoracionpostApi(request, id=0):
    if request.method == 'GET':
        valoracionpost = Valoracionpost.objects.all()
        valoracionpost_serializer = ValoracionpostSerializer(
            valoracionpost, many=True)
        return JsonResponse(valoracionpost_serializer.data, safe=False)

    elif request.method == 'POST':
        valoracionpost_data = JSONParser().parse(request)
        valoracionpost_serializer = ValoracionpostSerializer(
            data=valoracionpost_data)
        if valoracionpost_serializer.is_valid():
            valoracionpost_serializer.save()
            return JsonResponse("Add valoracion post", safe=False)
        return JsonResponse("Failed to add valoracion post", safe=False)

    elif request.method == 'PUT':
        valoracionpost_data = JSONParser().parse(request)
        valoracionpost = Valoracionpost.objects.get(
            ValoracionpostId=valoracionpost_data['ValoracionId'])
        valoracionpost_serializer = ValoracionpostSerializer(
            valoracionpost, data=valoracionpost_data)
        if valoracionpost_serializer.is_valid():
            valoracionpost_serializer.save()
            return JsonResponse("Update valoracion post", safe=False)
        return JsonResponse("Failed to update valoracion post", safe=False)

    elif request.method == 'DELETE':
        valoracionpost = Valoracionpost.objects.get(ValoracionId=id)
        valoracionpost.delete()
        return JsonResponse("Delete valoracion post", safe=False)


@csrf_exempt
def valoracioncomentariosApi(request, id=0):
    if request.method == 'GET':
        valoracioncomentarios = Valoracioncomentarios.objects.all()
        valoracioncomentarios_serializer = ValoracioncomentariosSerializer(
            valoracioncomentarios, many=True)
        return JsonResponse(valoracioncomentarios_serializer.data, safe=False)

    elif request.method == 'POST':
        valoracioncomentarios_data = JSONParser().parse(request)
        valoracioncomentarios_serializer = ValoracioncomentariosSerializer(
            data=valoracioncomentarios_data)
        if valoracioncomentarios_serializer.is_valid():
            valoracioncomentarios_serializer.save()
            return JsonResponse("Add valoracion comentarios", safe=False)
        return JsonResponse("Failed to add valoracion comentarios", safe=False)

    elif request.method == 'PUT':
        valoracioncomentarios_data = JSONParser().parse(request)
        valoracioncomentarios = Valoracioncomentarios.objects.get(
            ValoracioncomentariosId=valoracioncomentarios_data['ValoracionId'])
        valoracioncomentarios_serializer = ValoracioncomentariosSerializer(
            valoracioncomentarios, data=valoracioncomentarios_data)
        if valoracioncomentarios_serializer.is_valid():
            valoracioncomentarios_serializer.save()
            return JsonResponse("Update valoracion comentarios", safe=False)
        return JsonResponse("Failed to update valoracion comentarios", safe=False)

    elif request.method == 'DELETE':
        valoracioncomentarios = Valoracioncomentarios.objects.get(
            ValoracionId=id)
        valoracioncomentarios.delete()
        return JsonResponse("Delete valoracion comentarios", safe=False)


@csrf_exempt
def check(request):
    if request.user.is_authenticated:
        return JsonResponse("Si auth", safe=False)
    else:
        return JsonResponse("No login", safe=False, status=401)


@csrf_exempt
def login(request):
    usuario_data = JSONParser().parse(request)
    username = usuario_data['Correo']
    password = usuario_data['password']
    user = auth.authenticate(Correo=username, password=password)
    if user is not None:
        auth.login(request, user)
        return JsonResponse("Login correcto ", safe=False)
    else:
        return JsonResponse("Error login uwu", safe=False, status=401)


@csrf_exempt
def logout(request):
    auth.logout(request)
    return JsonResponse("Logout correcto uwu", safe=False, status=401)


def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


def index(request, path=''):
    return render(request, 'index.html')
