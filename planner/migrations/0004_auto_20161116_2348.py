# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_advisor_co_req_courses_department_instructor_pre_req_schedules_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='courses',
            name='dept_name',
            field=models.CharField(max_length=30),
        ),
    ]
