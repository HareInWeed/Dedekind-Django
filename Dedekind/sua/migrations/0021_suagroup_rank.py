# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-14 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sua', '0020_auto_20171014_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='suagroup',
            name='rank',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
