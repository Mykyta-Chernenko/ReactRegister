# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='staff',
            field=models.CharField(choices=[('T', 'Teacher'), ('S', 'Student'), ('A', 'Admin')], max_length=1),
        ),
    ]
