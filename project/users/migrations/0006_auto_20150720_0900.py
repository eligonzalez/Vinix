# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150720_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressuser',
            name='addressDefault',
            field=models.BooleanField(default=True),
        ),
    ]
