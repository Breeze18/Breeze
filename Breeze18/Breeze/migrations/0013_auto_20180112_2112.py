# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-12 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Breeze', '0012_accomregistration_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='subCategoryName',
            field=models.CharField(default='', help_text='Proper name of subcategory. eg. Music, Business and Entrepreneurship', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='contact_market',
            field=models.CharField(blank=True, help_text='Marketing representative', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='contact_pr',
            field=models.CharField(blank=True, help_text='PR representative', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='contact_spons',
            field=models.CharField(blank=True, help_text='Sponsorship representative', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='subCategory',
            field=models.CharField(help_text='In lowercase, without any space. e.g. music, drama', max_length=50),
        ),
    ]
