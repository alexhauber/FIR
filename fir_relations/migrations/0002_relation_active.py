# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-26 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir_relations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]