# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-10 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthMonitoring', '0026_heartratedata_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperaturedata',
            name='status',
            field=models.CharField(choices=[('HP', 'Hypothermia'), ('NT', 'Normal'), ('FE', 'Fever'), ('HX', 'Hyperpyrexia')], default='NT', max_length=4),
        ),
    ]
