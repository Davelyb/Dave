# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-20 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20180120_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]