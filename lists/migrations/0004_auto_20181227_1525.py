# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-27 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='list',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='list',
            name='text',
            field=models.TextField(default=''),
        ),
    ]