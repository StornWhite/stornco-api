# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20170201_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
