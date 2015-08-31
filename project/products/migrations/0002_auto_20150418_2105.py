# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='type',
            field=models.CharField(choices=[('B', 'blanco'), ('T', 'tinto'), ('R', 'rosado'), ('E', 'espumoso')], max_length=1, blank=True, default=False),
        ),
    ]
