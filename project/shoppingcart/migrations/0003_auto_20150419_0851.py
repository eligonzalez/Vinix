# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0002_shopping_cart_ammount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopping_cart',
            old_name='ammount',
            new_name='amount',
        ),
    ]
