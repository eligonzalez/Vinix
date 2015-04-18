from django.db import models


class Cellar(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Zone(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Varietal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="static/images/shop/products")

    def __str__(self):
        return self.name


class Wine(Product):
    size = models.CharField(max_length=50, blank=True)
    alcohol = models.DecimalField(max_digits=4,decimal_places=2)
    temperature = models.DecimalField(max_digits=4,decimal_places=2)
    elaboration = models.CharField(max_length=1000, blank=True)
    cellar = models.ForeignKey('Cellar', blank=True)
    zone = models.ForeignKey('Zone', blank=True)
    country = models.ForeignKey('Country', blank=True)
    varietal = models.ForeignKey('Varietal', blank=True)
    style = models.CharField(max_length=40, blank=True)
    TYPE = (
        ('B', 'Blanco'),
        ('T', 'Tinto'),
        ('R', 'rosado'),
        ('E', 'espumoso'),
    )
    type = models.CharField(max_length=1, choices=TYPE, default=False, blank=True)

