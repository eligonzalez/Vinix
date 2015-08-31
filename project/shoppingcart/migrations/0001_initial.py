# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20150418_2246'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('product', models.ForeignKey(to='products.Product')),
                ('user', models.ForeignKey(to='users.BasicUser')),
            ],
        ),
    ]
