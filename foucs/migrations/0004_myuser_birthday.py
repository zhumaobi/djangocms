# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foucs', '0003_auto_20170808_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(null=True, verbose_name='birthday'),
        ),
    ]
