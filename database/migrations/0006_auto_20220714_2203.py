# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-14 15:03
from __future__ import unicode_literals

import database.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20220712_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='category',
            field=models.CharField(choices=[('Pneumonia', 'Pneumonia'), ('Tuberculosis', 'Tuberculosis'), ('Covid19', 'COVID19'), ('Normal', 'Normal')], default='database', max_length=100),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='database/images'),
        ),
    ]
