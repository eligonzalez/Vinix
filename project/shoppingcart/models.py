from django.db import models
from users.models import BasicUser
from products.models import Product

class Shopping_Cart(models.Model):
    user = models.ForeignKey(BasicUser)
    product = models.ForeignKey(Product)
    ammount = models.IntegerField(default=1)

    @classmethod
    def get_products(self, user):
        res = []
        for item in Shopping_Cart.objects.filter(user=user):
            res.append(item.product)
        return res

    @classmethod
    def get_number(self, user):
        return len(Shopping_Cart.objects.filter(user=user))

    @classmethod
    def get_ammount(self, user):
        return sum(map(lambda x: x.product.price*x.ammount, Shopping_Cart.objects.filter(user=user)))
