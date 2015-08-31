# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150418_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='marriage',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='wine',
            name='temperature',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
