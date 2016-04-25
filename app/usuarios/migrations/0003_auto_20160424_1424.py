# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20160423_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='set_password',
            field=models.BooleanField(default=False, verbose_name='\xbfContrase\xf1a encriptada?'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='codigo',
            field=models.CharField(blank=True, max_length=120, verbose_name='uuid'),
        ),
    ]