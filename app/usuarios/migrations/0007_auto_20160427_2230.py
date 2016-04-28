# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-28 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20160425_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, db_index=True, max_length=20, unique=True, verbose_name='Key')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(auto_now=True, default='2016-12-12 12:12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='lastname',
            field=models.CharField(blank=True, max_length=120, verbose_name='apellido'),
        ),
        migrations.AddField(
            model_name='token',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_token', to='usuarios.Usuario'),
        ),
    ]