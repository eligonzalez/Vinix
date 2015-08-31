# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20150418_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='alcohol',
            field=models.DecimalField(default=None, decimal_places=2, max_digits=4, blank=True),
        ),
    ]
