# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-07 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscar_promotions', '0003_timebasedpromotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='timebasedpromotion',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]