# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demosky', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensors',
            name='sensor_id',
            field=models.CharField(max_length=100),
        ),
    ]
