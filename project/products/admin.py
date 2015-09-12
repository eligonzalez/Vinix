from django.contrib import admin
from .models import *
# Register your models here.

class ShowProduct(admin.ModelAdmin):
	list_display = ['name', 'price', 'image', 'zone', 'country', 'elaboration', 'alcohol']

class ShowWine(admin.ModelAdmin):
	list_display = ['name', 'price', 'image', 'zone', 'country', 'elaboration', 'alcohol', 'size', 'temperature', 'cellar', 'varietal', 'style', 'marriage', 'type']

class ShowSpirit(admin.ModelAdmin):
	list_display = ['type', 'subType']

class ShowFavoriteProduct(admin.ModelAdmin):
	list_display = ['id', 'user', 'product']

admin.site.register(Cellar)
admin.site.register(Country)
admin.site.register(Zone)
admin.site.register(Varietal)
admin.site.register(SubTypeSpirit)
admin.site.register(Style)
admin.site.register(Product, ShowProduct)
admin.site.register(Wine, ShowWine)
admin.site.register(Spirit, ShowSpirit)
admin.site.register(FavoriteProduct, ShowFavoriteProduct)