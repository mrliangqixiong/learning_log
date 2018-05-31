# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-31 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.CharField(max_length=200, verbose_name='内容'),
        ),
    ]