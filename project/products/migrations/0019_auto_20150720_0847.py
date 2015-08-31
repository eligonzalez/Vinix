# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20150708_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='type',
            field=models.CharField(choices=[('B', 'Blanco'), ('T', 'Tinto'), ('R', 'Rosado'), ('E', 'Espumoso')], blank=True, max_length=1, default=False),
        ),
    ]
