# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-29 11:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HealthMonitoring', '0019_auto_20180529_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature_reading', models.DecimalField(decimal_places=2, max_digits=3)),
                ('data_recorded', models.DateField(default=datetime.date.today)),
                ('data_from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthMonitoring.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='heartratedata',
            name='date_recorded',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
