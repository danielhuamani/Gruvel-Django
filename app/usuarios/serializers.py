
from .models import Usuario
from rest_framework import serializers


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('name', 'lastname', 'email', 'password')
