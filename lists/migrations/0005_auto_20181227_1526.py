# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-27 23:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20181227_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='list',
        ),
        migrations.RemoveField(
            model_name='list',
            name='text',
        ),
    ]
