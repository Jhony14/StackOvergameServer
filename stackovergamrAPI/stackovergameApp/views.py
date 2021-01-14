from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from stackovergameApp.models import Tipousuario, Usuario, Post, Comentarios, Imagenespost, Imagenescomentarios, Valoracionpost, Valoracioncomentarios
from stackovergameApp.serializers import TipousuarioSerializer, UsuarioSerializer, PostSerializer, ComentariosSerializer, ImagenespostSerializer, ImagenescomentariosSerializer, ValoracionpostSerializer, ValoracioncomentariosSerializer

from django.core.files.storage import default_storage

# Create your views here.


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
def usuarioApi(request, id=0):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuario, many=True)

        return JsonResponse(usuario_serializer.data, safe=False)

    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(
            data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Add usuario", safe=False)
        return JsonResponse("Failed to add usuario", safe=False)

    elif request.method == 'PUT':
        usuario_data = JSONParser().parse(request)
        usuario = Usuario.objects.get(
            UsuarioId=usuario_data['UsuarioId'])
        usuario_serializer = UsuarioSerializer(
            usuario, data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Update usuario", safe=False)
        return JsonResponse("Failed to update usuario", safe=False)

    elif request.method == 'DELETE':
        usuario = Usuario.objects.get(UsuarioId=id)
        usuario.delete()
        return JsonResponse("Delete usuario", safe=False)


@csrf_exempt
def postApi(request, id=0):
    if request.method == 'GET':
        post = Post.objects.all()
        post_serializer = PostSerializer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)

    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(
            data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Add post", safe=False)
        return JsonResponse("Failed to add post", safe=False)

    elif request.method == 'PUT':
        post_data = JSONParser().parse(request)
        post = Post.objects.get(
            PostId=post_data['PostId'])
        post_serializer = PostSerializer(
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
def comentariosApi(request, id=0):
    if request.method == 'GET':
        comentarios = Comentarios.objects.all()
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
def login(request):
    if request.method == 'POST':
        user = JSONParser().parse(request)
        try:
            userdetails = Usuario.objects.get(
                UsuarioLogin=user['UsuarioLogin'], UsuarioPassword=user['UsuarioPassword'])
            return JsonResponse("Login", safe=False)
        except Usuario.DoesNotExist:
            return JsonResponse("Error login", safe=False)




@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
