from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from app.core.utils import encrypt_password
from .models import Usuario
from .serializers import UsuarioSerializer
import json


def usuarios(request):
    data = {'status': 200}
    # METODOS
    if request.method == "GET":
        listado_usuario = list(Usuario.objects.all().values('email', 'nombre', 'apellido'))
        data['usuarios'] = listado_usuario
    if request.method == "POST":
        data = json.loads(request.body)
        email = data['email']
        nombre = data['name']
        apellido = data['lastname']
        password = data['password']
        password_encrypt = encrypt_password(password)
        try:
            usuario = Usuario(email=email, nombre=nombre, apellido=apellido, password=password_encrypt).save()
            data = {'status': 200}
            print "dadas"
        except Exception, e:
            data = {'status': 500}
            print  "error"
    return JsonResponse(data)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
