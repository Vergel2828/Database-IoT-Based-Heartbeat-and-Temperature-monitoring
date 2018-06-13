# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-24 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthMonitoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='emailaddress_name',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='temperature',
            field=models.FloatField(),
        ),
    ]
