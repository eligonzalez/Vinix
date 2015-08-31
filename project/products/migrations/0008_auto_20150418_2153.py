# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150418_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spirit',
            old_name='tipe',
            new_name='tipee',
        ),
    ]
