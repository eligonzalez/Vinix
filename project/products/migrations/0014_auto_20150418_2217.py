# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20150418_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='wine',
            name='style',
            field=models.CharField(blank=True, verbose_name='Style', max_length=50),
        ),
    ]
