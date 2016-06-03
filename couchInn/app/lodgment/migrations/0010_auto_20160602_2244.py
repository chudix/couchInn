# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lodgment', '0009_auto_20160602_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodgment',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lodgment.Place', verbose_name='Lugar'),
        ),
    ]
