# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='city',
            field=models.CharField(default=7.5, max_length=255, verbose_name='city'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='university',
            name='country',
            field=models.CharField(max_length=255, verbose_name='country'),
        ),
    ]
