# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20150418_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='alcohol',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
    ]
