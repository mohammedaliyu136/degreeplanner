# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major_option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='school_option',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]