from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

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

class SubTypeSpirit(models.Model):
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
    image = models.ImageField(upload_to="images/")
    zone = models.ForeignKey('Zone', blank=True, default=None)
    country = models.ForeignKey('Country', blank=True, default=None)
    elaboration = models.CharField(max_length=1000, blank=True, default=None)
    alcohol = models.CharField(max_length=1000, blank=True, default=None)
    def __str__(self):
        return self.name

    @classmethod
    def get_general(self) :
        prodZone = Zone.objects.all()
        prodStyle = Style.objects.all()
        prodVarietal = Varietal.objects.all()
        destYLicor = SubTypeSpirit.objects.all()
        return {'prodZone': prodZone,'prodStyle':prodStyle, 'prodVarietal':prodVarietal, 'destYLicor':destYLicor}


    @classmethod
    def get_pagination(self,request,products, number) :
        paginator = Paginator(products, number)
        page = request.GET.get('page')

        try:
            prod_page = paginator.page(page)
        except PageNotAnInteger:
            prod_page = paginator.page(1)
        except EmptyPage:
            prod_page = paginator.page(paginator.num_pages)
        return {'list_prod':prod_page}

class Wine(Product):
    size = models.CharField(max_length=50, blank=True)
    temperature = models.CharField(max_length=1000, blank=True)
    cellar = models.ForeignKey('Cellar', blank=True)
    varietal = models.ForeignKey('Varietal', blank=True)
    style = models.ForeignKey('Style', blank=True)
    marriage = models.CharField(max_length=1000, blank=True)
    TYPE = (
        ('B', 'Blanco'),
        ('T', 'Tinto'),
        ('R', 'Rosado'),
        ('E', 'Espumoso'),
    )
    type = models.CharField(max_length=1, choices=TYPE, default=False, blank=True)

    @classmethod
    def get_product_filter(self, filter, value):
        typeProd = None

        if filter == 'type' :
            prod = Wine.objects.filter(type=value)
            p = prod[0]
            typeProd = p.get_type_display()
        elif filter == 'zone' :
            prod = Product.objects.filter(zone__name=value)
            typeProd = 'por zona'
        elif filter == 'style' :
            prod = Wine.objects.filter(style__name=value)
            typeProd = 'por estilo'
        elif filter == 'varietal' :
            prod = Wine.objects.filter(varietal__name=value)
            typeProd = 'por variedad'
        elif filter == 'priceLower' :
            prod = Product.objects.filter(price__range=(0,9.99))
            typeProd = 'por menos de 10€'
        elif filter == 'priceUpper' :
            prod = Product.objects.filter(price__range=(10,20))
            typeProd = 'entre 10€ y 20€'

        return {'type' : typeProd, 'prod' : prod}


class Spirit(Product):
    TYPE = (
        ('D', 'Destilado'),
        ('L', 'Licor'),
    )
    type = models.CharField(max_length=1, choices=TYPE, default='D',blank=True)
    subType = models.ForeignKey(SubTypeSpirit,blank=True)