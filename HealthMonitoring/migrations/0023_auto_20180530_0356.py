# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-30 03:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HealthMonitoring', '0022_auto_20180530_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartratedata',
            name='data_from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='temperaturedata',
            name='data_from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
