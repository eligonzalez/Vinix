# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('lastName', models.CharField(max_length=50, blank=True)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('postalCode', models.CharField(max_length=5, blank=True)),
                ('town', models.CharField(max_length=50, blank=True)),
                ('province', models.CharField(max_length=50, blank=True)),
                ('addressDefault', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=50, blank=True, default='España')),
                ('phone', models.CharField(max_length=50, blank=True)),
                ('idUser', models.ForeignKey(to='users.BasicUser', db_column='_id')),
            ],
        ),
    ]
