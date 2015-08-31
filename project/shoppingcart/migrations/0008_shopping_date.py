# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0007_auto_20150429_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2015, 4, 29, 11, 31, 23, 839182, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
