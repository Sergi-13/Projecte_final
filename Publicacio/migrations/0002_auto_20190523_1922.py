# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicacio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personatge',
            name='text',
            field=models.TextField(max_length=5000),
        ),
    ]
