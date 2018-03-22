# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-19 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180117_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(blank=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
