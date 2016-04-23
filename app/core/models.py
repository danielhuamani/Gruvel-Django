# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class AuditableModel(models.Model):
    active = models.BooleanField('Activo', default=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        abstract = True
