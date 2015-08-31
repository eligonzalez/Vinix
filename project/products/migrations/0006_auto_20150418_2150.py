# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150418_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTipeSpirit',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='spirit',
            name='subTipe',
            field=models.ForeignKey(default=None, to='products.SubTipeSpirit', blank=True),
        ),
    ]
