# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegandb_app', '0005_auto_20171023_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='title',
            field=models.CharField(default='wiadomość', max_length=140, verbose_name='Tytuł'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messages',
            name='content',
            field=models.TextField(verbose_name='Treść'),
        ),
    ]