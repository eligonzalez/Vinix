# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20150418_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spirit',
            old_name='tipee',
            new_name='tipe',
        ),
    ]
