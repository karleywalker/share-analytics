# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 15:47
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='settings',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
