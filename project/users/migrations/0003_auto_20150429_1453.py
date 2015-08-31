# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_addressuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressuser',
            name='idUser',
            field=models.ForeignKey(to='users.BasicUser'),
        ),
    ]
