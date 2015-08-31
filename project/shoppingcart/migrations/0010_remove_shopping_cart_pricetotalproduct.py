# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0009_shopping_cart_pricetotalproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_cart',
            name='priceTotalProduct',
        ),
    ]
