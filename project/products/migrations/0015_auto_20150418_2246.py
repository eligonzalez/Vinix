# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20150418_2217'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubTipeSpirit',
            new_name='SubTypeSpirit',
        ),
        migrations.RenameField(
            model_name='spirit',
            old_name='subTipe',
            new_name='subType',
        ),
        migrations.RenameField(
            model_name='spirit',
            old_name='tipe',
            new_name='type',
        ),
    ]
