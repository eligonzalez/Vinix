# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0008_shopping_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='priceTotalProduct',
            field=models.DecimalField(max_digits=5, default=0, decimal_places=2, blank=True),
            preserve_default=False,
        ),
    ]
