# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0005_couchinnuser_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couchinnuser',
            name='gender',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=1),
        ),
    ]
