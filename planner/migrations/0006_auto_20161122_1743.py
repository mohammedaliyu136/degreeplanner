# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-22 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_degree_req'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='name',
        ),
        migrations.AddField(
            model_name='courses',
            name='course_credit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='academic_standing',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='classification',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='concentration',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='gpa',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='major',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='school',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='total_credit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='advisor',
            name='i_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='advisor',
            name='s_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='co_req',
            name='co_req_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='co_req',
            name='course_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='dept_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='degree_req',
            name='course_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='degree_req',
            name='major_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='building',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='dept_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='major_option',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='major_option',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='pre_req',
            name='course_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pre_req',
            name='pre_req_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='course_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='grade',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='student_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='year',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='school_option',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='school_option',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='dept_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
