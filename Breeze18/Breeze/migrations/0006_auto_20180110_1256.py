# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 12:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Breeze', '0005_forgetpass'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='transaction_status',
            field=models.CharField(default='Unpaid', max_length=200),
        ),
        migrations.AlterField(
            model_name='registration',
            name='transaction_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='registration',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
