# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20150708_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='style',
            field=models.CharField(blank=True, verbose_name='Style', max_length=50),
        ),
    ]
