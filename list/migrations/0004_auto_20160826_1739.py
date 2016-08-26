# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 21:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20160826_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ping',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ping',
            name='requester',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL),
        ),
    ]
