# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160304_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
