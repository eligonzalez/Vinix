from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cellar)
admin.site.register(Country)
admin.site.register(Zone)
admin.site.register(Varietal)
admin.site.register(Product)
admin.site.register(Wine)