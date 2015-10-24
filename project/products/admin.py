from django.contrib import admin
from .models import *
# Register your models here.

class ShowProduct(admin.ModelAdmin):
	list_display = ['id', 'name', 'price', 'image', 'zone', 'country', 'elaboration', 'alcohol', 'date']
	readonly_fields = ('id','date')

class ShowWine(admin.ModelAdmin):
	list_display = ['id', 'name', 'price', 'image', 'zone', 'country', 'elaboration', 'alcohol', 'size', 'temperature', 'cellar', 'varietal', 'style', 'marriage', 'type']
	readonly_fields = ('id',)

class ShowSpirit(admin.ModelAdmin):
	list_display = ['id', 'name', 'price', 'image', 'zone', 'country', 'elaboration', 'alcohol','type', 'subType']
	readonly_fields = ('id',)

class ShowFavoriteProduct(admin.ModelAdmin):
	list_display = ['id', 'user', 'product']
	readonly_fields = ('id',)

class ShowCellar(admin.ModelAdmin):
	list_display = ['id', 'name']
	readonly_fields = ('id',)

class ShowCountry(admin.ModelAdmin):
	list_display = ['id', 'name']
	readonly_fields = ('id',)

class ShowZone(admin.ModelAdmin):
	list_display = ['id', 'name']
	readonly_fields = ('id',)

class ShowVarietal(admin.ModelAdmin):
	list_display = ['id', 'name']
	readonly_fields = ('id',)

class ShowSubTypeSpirit(admin.ModelAdmin):
	list_display = ['id', 'name']
	readonly_fields = ('id',)

class ShowStyle(admin.ModelAdmin):
	list_display = ['id', 'name']
	readonly_fields = ('id',)

class ShowPunctuationProduct(admin.ModelAdmin):
	list_display = ['id', 'user', 'product', 'comment', 'punctuation', 'date']
	readonly_fields = ('id', 'date')

admin.site.register(Cellar, ShowCellar)
admin.site.register(Country, ShowCountry)
admin.site.register(Zone, ShowZone)
admin.site.register(Varietal, ShowVarietal)
admin.site.register(SubTypeSpirit, ShowSubTypeSpirit)
admin.site.register(Style, ShowStyle)
admin.site.register(Product, ShowProduct)
admin.site.register(Wine, ShowWine)
admin.site.register(Spirit, ShowSpirit)
admin.site.register(FavoriteProduct, ShowFavoriteProduct)
admin.site.register(PunctuationProduct, ShowPunctuationProduct)

