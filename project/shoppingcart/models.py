from django.db import models
from users.models import BasicUser
from products.models import Product

class Shopping_Cart(models.Model):
    user = models.ForeignKey(BasicUser)
    product = models.ForeignKey(Product)
    amount = models.IntegerField(default=1)

    @classmethod
    def get_products(self, user):
        return Shopping_Cart.objects.filter(user=user)

    @classmethod
    def get_number(self, user):
        return len(Shopping_Cart.objects.filter(user=user))

    @classmethod
    def get_amount(self, user):
        return sum(map(lambda x: x.product.price*x.amount, Shopping_Cart.objects.filter(user=user)))
