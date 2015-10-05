from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from users.models import BasicUser


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
    date = models.DateField(auto_now_add=True, blank=True)
    def __str__(self):
        return str(self.id)

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


class Spirit(Product):
    TYPE = (
        ('D', 'Destilado'),
        ('L', 'Licor'),
    )
    type = models.CharField(max_length=1, choices=TYPE, default='D',blank=True)
    subType = models.ForeignKey(SubTypeSpirit,blank=True)

    @classmethod
    def get_products_filter(self, value):
        typeProd = value
        prod = Spirit.objects.filter(subType__name=value)
        return {'type' : typeProd, 'prod' : prod}

class FavoriteProduct(models.Model):
    user = models.ForeignKey(BasicUser)
    product = models.ForeignKey(Product)

    @classmethod
    def get_products_favorite(self, u):

        prod_favorite = FavoriteProduct.objects.filter(user=u)
        productsFavorite = []

        for p in prod_favorite:
            productsFavorite.append(Product.objects.get(id=str(p.product.id)))

        return {'user': u, 'productsFavorite': productsFavorite}

    @classmethod
    def add_product_favorite(self, idProduct, u):
        p = Product.objects.get(id=str(idProduct))
        user = BasicUser.objects.get(id=u.id)

        if not FavoriteProduct.objects.filter(user=user, product=p).exists():
            ad = FavoriteProduct(user=user, product=p)
            ad.save()
        #else:
            #Mensaje de error

    @classmethod
    def delete_product_favorite(self, idProduct, u):
        r = FavoriteProduct.objects.filter(user=u, product=idProduct)
        r.delete()

class PunctuationProduct(models.Model):
    user = models.ForeignKey(BasicUser)
    product = models.ForeignKey(Product)
    comment = models.CharField(max_length=1000, blank=True, default=None)
    punctuation = models.IntegerField()
    date = models.DateField(auto_now_add=True, blank=True)


    @classmethod
    def favorite_punctuation_product(self, user):
        favorite = FavoriteProduct.objects.filter(user=user)

        for f in favorite:
            suma = 0
            punct = PunctuationProduct.objects.filter(product=f.product)

            for p in punct:
                suma = suma + p.punctuation

            if len(punct) > 0:
                f.product.punctuation = suma/len(punct)
            else:
                f.product.punctuation = -1

        return {'favorite': favorite}

    @classmethod
    def add_comment(self, p, comment, punctuation, user):
        u = BasicUser.objects.get(id=user.id)

        if not PunctuationProduct.objects.filter(user=user, product=p).exists():
            newComment = PunctuationProduct(user=u, product=p, comment=comment, punctuation=punctuation)
            newComment.save()

    @classmethod
    def delete_comment(self, p, user_id, reqUser):
        if str(reqUser.id) == str(user_id):
            user = BasicUser.objects.get(id=user_id)

            comment = PunctuationProduct.objects.filter(user=user, product=p)
            comment.delete()