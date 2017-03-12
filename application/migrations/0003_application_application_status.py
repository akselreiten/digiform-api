# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20170312_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='application_status',
            field=models.IntegerField(choices=[(0, 'Processing'), (1, 'Accepted'), (2, 'Declined')], default=0),
        ),
    ]
