# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-21 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Student'),
        ),
    ]