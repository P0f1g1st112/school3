# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_auto_20170829_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
    ]
