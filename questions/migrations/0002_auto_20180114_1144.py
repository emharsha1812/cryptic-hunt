# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='id',
        ),
        migrations.AlterField(
            model_name='level',
            name='level_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
