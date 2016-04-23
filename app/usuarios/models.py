# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from uuid import uuid4
from app.core.models import AuditableModel
from app.core.utils import validad_password


class Usuario(AuditableModel):
    email = models.EmailField("Email")
    nombre = models.CharField("nombre", max_length=120)
    apellido = models.CharField("apellido", max_length=120)
    password = models.CharField("Password", max_length=120)
    codigo = models.CharField("uuid", max_length=120)

    class Meta:
        verbose_name = "Usuarios"
        verbose_name_plural = "Usuarios"

    def save(self, *args, **kwargs):
        error_codigo = False
        if not self.codigo:
            error_codigo = True
        while error_codigo:
            self.codigo = str(uuid4())[:16]
            if not Usuarios.objects.filter(codigo=self.codigo).exists():
                error_codigo = False
        super(Usuario, self).save(*args, **kwargs)

    def get_full_name(self):
        return self.nombre

    def is_authenticated(self):
        return True

    def is_password_valid(self, password):
        return validad_password(password, self.password)

    def __unicode__(self):
        return self.nombre
