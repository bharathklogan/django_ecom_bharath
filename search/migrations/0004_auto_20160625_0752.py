# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-25 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20160625_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='in_stock',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]