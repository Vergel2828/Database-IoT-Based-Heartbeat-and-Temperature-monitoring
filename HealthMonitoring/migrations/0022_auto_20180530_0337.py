# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-30 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthMonitoring', '0021_auto_20180530_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2),
        ),
    ]
