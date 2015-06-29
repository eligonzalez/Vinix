from django.db import models
from users.models import BasicUser
from products.models import *

class Shopping(models.Model):
    user = models.ForeignKey(BasicUser)
    address = models.CharField(max_length=50,blank=True)
    priceTotal = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    finish = models.BooleanField(default=True, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_products(self, user):
        shop = Shopping.objects.filter(user=2, finish=False)
        print (shop)
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
        shop = Shopping.objects.filter(user=2, finish=False)
        return sum(map(lambda x: x.product.price*x.amount, Shopping_Cart.objects.filter(shopping=shop)))


class Shopping_Cart(models.Model):
    shopping = models.ForeignKey(Shopping, default=None)
    product = models.ForeignKey(Product)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

