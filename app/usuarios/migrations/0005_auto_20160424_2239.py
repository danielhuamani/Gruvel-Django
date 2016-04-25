# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20160424_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nickname',
            field=models.CharField(max_length=120, verbose_name='nickname', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(unique=True, max_length=75, verbose_name='Email'),
            preserve_default=True,
        ),
    ]
