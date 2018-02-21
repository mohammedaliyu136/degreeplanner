# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-12 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0025_schedules_course_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultSchedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10, null=True)),
                ('course_title', models.CharField(max_length=50, null=True)),
                ('semester', models.CharField(max_length=20, null=True)),
                ('major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='major_schedule', to='planner.Major_option')),
            ],
        ),
    ]