# -*- coding: utf-8 -*-
from uuid import uuid4
from .models import Token

LONGITUD_DE_TOKEN = 32


def genera_token(usuario):
    ''' Genera un token para un usuario '''
    error = True

    # generamos un token único
    while error:
        print str(uuid4())
        _uuid = str(uuid4()).replace('-', '')[:LONGITUD_DE_TOKEN]
        token = Token(usuario=usuario, key=_uuid)
        try:
            token.save()
            error = False
        except:
            pass

    return token
