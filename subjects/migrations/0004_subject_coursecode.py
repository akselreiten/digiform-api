# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_subject_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='courseCode',
            field=models.CharField(default='TMA4100', max_length=10, verbose_name=b'course code'),
            preserve_default=False,
        ),
    ]
