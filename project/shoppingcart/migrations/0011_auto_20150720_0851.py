# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0010_remove_shopping_cart_pricetotalproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping',
            name='address',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='priceTotal',
            field=models.DecimalField(decimal_places=2, null=True, default=0, max_digits=5, blank=True),
        ),
        migrations.AlterField(
            model_name='shopping_cart',
            name='amount',
            field=models.IntegerField(null=True, default=1, blank=True),
        ),
    ]
