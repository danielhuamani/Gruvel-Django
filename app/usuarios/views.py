# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.contrib.auth import authenticate

from .models import Usuario
from .utils import genera_token
from app.core.utils import encrypt_password
from .serializers import UsuarioSerializer

import json
from .utils import genera_token


@csrf_exempt
def usuarios(request):
    data = {'status': 200}
    # METODOS
    if request.method == "GET":
        listado_usuario = list(Usuario.objects.all().values('email', 'name', 'lastname'))
        data['usuarios'] = listado_usuario
    if request.method == "POST":
        data = json.loads(request.body)
        email = data['email']
        nombre = data['name']

        password = data['password']
        try:
            usuario = Usuario(email=email, name=nombre, password=password).save()
            data = {'status': 200}
            print "dadas"
        except Exception, e:
            data = {'status': 500}
    return JsonResponse(data)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


@csrf_exempt
def login(request, id=None):
    ''' Autentica a un usuario y retorna un token

        curl --data "username=demo@demo.com&password=demodemo http://127.0.0.1:8000/sistema/api/login/
    '''
    data = {'status': 500}
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            Usuario.objects.get(email=email)
            usuario_valido = True
        except Usuario.DoesNotExist:
            data['msg'] = 'El usuario no existe'
            usuario_valido = False
            data['status'] = 500
        usuario = None
        if usuario_valido:
            usuario = authenticate(username=email, password=password)
            if not usuario:
                data['msg'] = u'El usuario + contraseña son inválidos'

        if usuario:
            data['status'] = 200
            token = genera_token(usuario)
            data['usuario'] = {
                'nickname': usuario.nickname,
                'email': usuario.email,
                'name': usuario.name,
                'lastname': usuario.lastname,

            }
            data['token'] = token.key

    return JsonResponse(data)
