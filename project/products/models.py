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

class SubTipeSpirit(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Style(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="static/images/shop/products")
    zone = models.ForeignKey('Zone', blank=True, default=None)
    country = models.ForeignKey('Country', blank=True, default=None)
    elaboration = models.CharField(max_length=1000, blank=True, default=None)
    alcohol = models.CharField(max_length=1000, blank=True, default=None)
    def __str__(self):
        return self.name

class Wine(Product):
    size = models.CharField(max_length=50, blank=True)
    temperature = models.CharField(max_length=1000, blank=True)
    cellar = models.ForeignKey('Cellar', blank=True)
    varietal = models.ForeignKey('Varietal', blank=True)
    style = models.CharField('Style', max_length=50, blank=True)
    marriage = models.CharField(max_length=1000, blank=True)
    TYPE = (
        ('B', 'blanco'),
        ('T', 'tinto'),
        ('R', 'rosado'),
        ('E', 'espumoso'),
    )
    type = models.CharField(max_length=1, choices=TYPE, default=False, blank=True)

class Spirit(Product):
    TIPE = (
        ('D', 'Destilado'),
        ('L', 'Licor'),
    )
    tipe = models.CharField(max_length=1, choices=TIPE, default='D',blank=True)
    subTipe = models.ForeignKey(SubTipeSpirit,blank=True)