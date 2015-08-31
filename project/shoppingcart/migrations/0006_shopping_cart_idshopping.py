# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0005_auto_20150429_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='idShopping',
            field=models.ForeignKey(default=None, to='shoppingcart.Shopping'),
        ),
    ]
