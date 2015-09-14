from django.contrib import admin
from .models import *

class ShowShopping_Cart(admin.ModelAdmin):
	list_display = ['id', 'shopping', 'product', 'amount']
	readonly_fields = ('id',)

class ShowShopping(admin.ModelAdmin):
	list_display = ['id', 'user', 'address', 'priceTotal', 'finish', 'date', 'lastName', 'address', 'postalCode', 'town', 'province', 'country', 'phone']
	readonly_fields = ('id', 'date')

admin.site.register(Shopping_Cart, ShowShopping_Cart)
admin.site.register(Shopping, ShowShopping)


