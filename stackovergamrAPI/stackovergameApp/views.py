from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from stackovergameApp.models import Tipousuario, Usuario, Post, Comentarios, Imagenespost, Imagenescomentarios, Valoracionpost, Valoracioncomentarios
from stackovergameApp.serializers import TipousuarioSerializer, UsuarioSerializer, PostSerializer, ComentariosSerializer, ImagenespostSerializer, ImagenescomentariosSerializer, ValoracionpostSerializer, ValoracioncomentariosSerializer


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
