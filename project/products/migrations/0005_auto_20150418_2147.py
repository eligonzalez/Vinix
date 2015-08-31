# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150418_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spirit',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, primary_key=True, to='products.Product')),
                ('tipee', models.CharField(blank=True, default='D', max_length=1, choices=[('D', 'Destilado'), ('L', 'Licor')])),
            ],
            bases=('products.product',),
        ),
        migrations.RemoveField(
            model_name='wine',
            name='alcohol',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='country',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='elaboration',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='zone',
        ),
        migrations.AddField(
            model_name='product',
            name='alcohol',
            field=models.DecimalField(max_digits=4, decimal_places=0, default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.ForeignKey(default=None, blank=True, to='products.Country'),
        ),
        migrations.AddField(
            model_name='product',
            name='elaboration',
            field=models.CharField(blank=True, max_length=1000, default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='zone',
            field=models.ForeignKey(default=None, blank=True, to='products.Zone'),
        ),
    ]
