from django.contrib import admin
from .models import *

class ShowShopping_Cart(admin.ModelAdmin):
	list_display = ['id', 'shopping', 'product', 'amount']

class ShowShopping(admin.ModelAdmin):
	list_display = ['id', 'user', 'address', 'priceTotal', 'finish']

admin.site.register(Shopping_Cart, ShowShopping_Cart)
admin.site.register(Shopping, ShowShopping)


