# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0006_shopping_cart_idshopping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopping_cart',
            old_name='idShopping',
            new_name='shopping',
        ),
        migrations.RemoveField(
            model_name='shopping_cart',
            name='user',
        ),
    ]
