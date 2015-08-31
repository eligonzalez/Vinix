# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('dni', models.CharField(max_length=12, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
