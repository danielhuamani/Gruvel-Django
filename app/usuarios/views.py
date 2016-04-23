from django.shortcuts import render
from django.http import JsonResponse
from app.core.utils import encrypt_password
from .models import Usuario


def usuarios(request):
    data = {'status': 200}
    # METODOS
    if request.method == "GET":
        listado_usuario = list(Usuario.objects.all().values('email', 'nombre', 'apellido'))
        data['usuarios'] = listado_usuario
    if request.method == "POST":
        email = request.POST.get("email")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        password = request.POST.get("password")
        password_encrypt = encrypt_password(password)
        try:
            usuario = Usuario(email=email, nombre=nombre, apellido=apellido, password=password_encrypt).save()
            data = {'status': 200}
        except Exception, e:
            data = {'status': 500}
    return JsonResponse(data)
