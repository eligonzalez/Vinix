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

class Shopping_Cart(models.Model):
    shopping = models.ForeignKey(Shopping, default=None)
    product = models.ForeignKey(Product)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)
    '''
    @classmethod
    def get_products(self, user):
        return Shopping_Cart.objects.filter(user=user)

    @classmethod
    def get_number(self, user):
        return len(Shopping_Cart.objects.filter(user=user))

    @classmethod
    def get_amount(self, user):
        return sum(map(lambda x: x.product.price*x.amount, Shopping_Cart.objects.filter(user=user)))
'''
