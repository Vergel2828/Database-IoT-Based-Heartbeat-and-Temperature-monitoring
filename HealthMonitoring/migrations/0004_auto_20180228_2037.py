# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-28 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthMonitoring', '0003_auto_20180228_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cellphone1',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cellphone2',
            field=models.CharField(max_length=11),
        ),
    ]
