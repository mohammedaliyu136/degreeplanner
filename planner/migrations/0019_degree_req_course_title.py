# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0018_auto_20161130_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree_req',
            name='course_title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
