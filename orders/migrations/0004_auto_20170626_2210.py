# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_merge_20170626_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
        migrations.AddField(
            model_name='orderline',
            name='line_item_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
