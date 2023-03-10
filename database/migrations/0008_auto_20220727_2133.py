# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-27 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20220714_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='category',
            field=models.CharField(blank=True, choices=[('Pneumonia', 'Pneumonia'), ('Tuberculosis', 'Tuberculosis'), ('COVID19', 'COVID19'), ('Normal', 'Normal')], max_length=100),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='gambar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
