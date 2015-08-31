# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150429_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressuser',
            name='address',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='country',
            field=models.CharField(blank=True, null=True, max_length=50, default='España'),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='lastName',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='name',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='phone',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='postalCode',
            field=models.CharField(blank=True, null=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='province',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='town',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
    ]
