# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-29 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthMonitoring', '0015_auto_20180526_1013'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HeartBeat',
        ),
        migrations.DeleteModel(
            name='Temperature',
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'Users Profile'},
        ),
    ]
