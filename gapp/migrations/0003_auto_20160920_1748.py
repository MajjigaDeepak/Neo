# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gapp', '0002_query_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='ques',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
