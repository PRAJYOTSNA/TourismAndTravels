# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_auto_20170703_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User',
            new_name='user',
        ),
    ]
