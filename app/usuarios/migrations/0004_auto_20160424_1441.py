# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20160424_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='apellido',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='name',
        ),
    ]
