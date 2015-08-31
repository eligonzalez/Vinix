# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cellar',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('image', models.ImageField(upload_to='static/images/shop/products')),
            ],
        ),
        migrations.CreateModel(
            name='Varietal',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, parent_link=True, to='products.Product')),
                ('size', models.CharField(max_length=50, blank=True)),
                ('alcohol', models.DecimalField(max_digits=4, decimal_places=2)),
                ('temperature', models.DecimalField(max_digits=4, decimal_places=2)),
                ('elaboration', models.CharField(max_length=1000, blank=True)),
                ('style', models.CharField(max_length=40, blank=True)),
                ('type', models.CharField(max_length=1, default=False, blank=True, choices=[('B', 'Blanco'), ('T', 'Tinto'), ('R', 'rosado'), ('E', 'espumoso')])),
                ('cellar', models.ForeignKey(to='products.Cellar', blank=True)),
                ('country', models.ForeignKey(to='products.Country', blank=True)),
                ('varietal', models.ForeignKey(to='products.Varietal', blank=True)),
                ('zone', models.ForeignKey(to='products.Zone', blank=True)),
            ],
            bases=('products.product',),
        ),
    ]
