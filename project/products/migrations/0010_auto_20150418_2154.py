# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20150418_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='alcohol',
            field=models.DecimalField(blank=True, max_digits=4, default=None, decimal_places=0),
        ),
    ]
