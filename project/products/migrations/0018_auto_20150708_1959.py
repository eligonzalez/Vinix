# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20150708_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='style',
            field=models.ForeignKey(to='products.Style', blank=True),
        ),
    ]
