# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150720_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicuser',
            name='dni',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
