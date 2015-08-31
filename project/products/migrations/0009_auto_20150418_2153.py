# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150418_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spirit',
            name='subTipe',
            field=models.ForeignKey(blank=True, to='products.SubTipeSpirit'),
        ),
    ]
