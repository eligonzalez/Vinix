# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_addressuser'),
        ('shoppingcart', '0004_shoppings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=50)),
                ('priceTotal', models.DecimalField(decimal_places=2, blank=True, max_digits=5)),
                ('finish', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to='users.BasicUser')),
            ],
        ),
        migrations.RemoveField(
            model_name='shoppings',
            name='user',
        ),
        migrations.DeleteModel(
            name='Shoppings',
        ),
    ]
