# -*- coding: utf-8 -*-
from django.conf import settings
from pbkdf2 import crypt
import re

SECRET_KEY = settings.SECRET_KEY
SALT = ''.join(re.findall("[a-zA-Z0-9]+", SECRET_KEY))
NUMERO_DE_ITERACIONES = 500


def encrypt_password(password):
    ''' Encripta la contraseña '''
    print SALT
    print password
    print NUMERO_DE_ITERACIONES
    return crypt(password, SALT, NUMERO_DE_ITERACIONES)


def validad_password(password, encoded):
    ''' Contrasta la contraseña brindada con el valor encriptado '''
    return encrypt_password(password) == encoded
