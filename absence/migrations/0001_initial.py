# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marks', '0002_mark'),
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('scheduledsubject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='timetable.ScheduledSubject')),
                ('value', models.CharField(default='н', max_length=1, verbose_name='absence')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='marks.Student')),
            ],
            bases=('timetable.scheduledsubject',),
        ),
    ]
