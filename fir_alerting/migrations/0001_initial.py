# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('incidents', '0003_auto_20160119_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('subject', models.TextField()),
                ('incident_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidents.IncidentCategory')),
            ],
            options={
                'db_table': 'incidents_categorytemplate',
            },
        ),
        migrations.CreateModel(
            name='RecipientTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('behalf', models.CharField(max_length=100)),
                ('recipient_to', models.TextField()),
                ('recipient_cc', models.TextField()),
                ('recipient_bcc', models.TextField(blank=True, null=True)),
                ('business_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='incidents.BusinessLine')),
            ],
            options={
                'db_table': 'incidents_recipienttemplate',
            },
        ),
    ]