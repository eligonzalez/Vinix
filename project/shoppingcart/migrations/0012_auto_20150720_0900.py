# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0011_auto_20150720_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping',
            name='finish',
            field=models.BooleanField(default=False),
        ),
    ]
