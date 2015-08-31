# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='ammount',
            field=models.IntegerField(default=1),
        ),
    ]
