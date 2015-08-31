# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20150418_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='alcohol',
            field=models.CharField(max_length=1000, blank=True, default=None),
        ),
    ]
