# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_addressuser'),
        ('shoppingcart', '0003_auto_20150419_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoppings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('priceTotal', models.DecimalField(decimal_places=2, max_digits=5, blank=True)),
                ('finish', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to='users.BasicUser')),
            ],
        ),
    ]
