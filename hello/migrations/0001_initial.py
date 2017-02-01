# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Echo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(db_index=True, max_length=50, unique=True)),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Echos',
                'verbose_name': 'Echo',
            },
        ),
    ]
