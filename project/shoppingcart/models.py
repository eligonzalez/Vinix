from django.db import models
from users.models import BasicUser
from products.models import *
import datetime
from dateutil.relativedelta import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

today = datetime.datetime.today()

class Shopping(models.Model):
    user = models.ForeignKey(BasicUser)
    address = models.CharField(max_length=50,blank=True, null=True)
    priceTotal = models.DecimalField(max_digits=5,default=0,decimal_places=2,blank=True, null=True)
    finish = models.BooleanField(default=False, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    postalCode = models.CharField(max_length=5, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, default='España', blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_products(self, user):
        shop = Shopping.objects.filter(user=user, finish=False)
        products = Shopping_Cart.objects.filter(shopping=shop)
        return products

    @classmethod
    def get_pricexAmount_product(self, shopping):
        pricexAmount = []
        for s in shopping:
            price = s.product.price*s.amount
            pricexAmount.append(price)
        return pricexAmount

    @classmethod
    def get_number(self, user):
        shop = Shopping.objects.filter(user=user, finish=False)
        return len(Shopping_Cart.objects.filter(shopping=shop))

    @classmethod
    def get_amount(self, user):
        shop = Shopping.objects.filter(user=user, finish=False)
        return sum(map(lambda x: x.product.price*x.amount, Shopping_Cart.objects.filter(shopping=shop)))

    @classmethod
    def accept_purchase(self, user, dir, price):

        shop = Shopping.objects.get(user=user, finish=False)
        products = Shopping_Cart.objects.filter(shopping=shop)

        subject, from_email, to = 'Compra finalizada', 'jordi.montes.sanabria@gmail.com', 'eli.gonzalez05@gmail.com'
        text_content = 'This is an important message.'
        html_products = ''
        for p in products:
            html_products += '<p>' + p.product.name + '</p><br>'

        html_content = html_products + '<p>This is an <strong>important</strong> message.</p>'
        shop.finish = True
        shop.priceTotal = price
        shop.name = dir.name
        shop.lastName = dir.lastName
        shop.address = dir.address
        shop.postalCode = dir.postalCode
        shop.town = dir.town
        shop.province = dir.province
        shop.country = dir.country
        shop.phone = dir.phone
        shop.save()
        new_shop = Shopping(user=user,date=today)
        new_shop.save()


        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


class Shopping_Cart(models.Model):
    shopping = models.ForeignKey(Shopping, default=None)
    product = models.ForeignKey(Product)
    amount = models.IntegerField(default=1,  blank=True, null=True)

    @property
    def total_product(self):
        return self.amount * self.product.price

    def __str__(self):
        return str(self.id)

    @classmethod
    def add_Product_Shopping_Cart(self, user, idProd, amount):
        shop = Shopping.objects.get(user=user, finish=False)
        exist = Shopping_Cart.objects.filter(product=idProd,shopping=shop).exists()
        product = Product.objects.get(id=idProd)

        if  not exist :
            newProduct = Shopping_Cart(shopping=shop, product=product, amount=amount)
            newProduct.save()
            return 0
        else :
            return 1
