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

    @classmethod
    def accept_purchase(self, user):
        shop = Shopping.objects.get(user=2, finish=False)
        shop.finish = True
        shop.save()
        new_shop = Shopping(user=2,address=shop.address,priceTotal=0,finish=False)
        new_shop.save()



class Shopping_Cart(models.Model):
    shopping = models.ForeignKey(Shopping, default=None)
    product = models.ForeignKey(Product)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @classmethod
    def add_Product_Shopping_Cart(self, user, idProd, amount):
        shop = Shopping.objects.get(user=2, finish=False)
        exist = Shopping_Cart.objects.filter(product=idProd,shopping=shop).exists()
        product = Product.objects.get(id=idProd)

        if  not exist :
            newProduct = Shopping_Cart(shopping=shop, product=product, amount=amount)
            newProduct.save()
            return 0
        else :
            return 1
