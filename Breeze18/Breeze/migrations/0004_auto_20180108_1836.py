# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Breeze', '0003_auto_20180108_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default='2018-02-09', help_text='Mention (start) date of the event'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default='B315', max_length=50),
        ),
    ]
