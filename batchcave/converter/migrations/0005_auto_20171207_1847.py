# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-07 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0004_auto_20171207_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversion',
            name='Type',
            field=models.IntegerField(choices=[('000', 'None')], default=0),
        ),
    ]
