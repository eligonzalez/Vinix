from django.contrib import admin
from users.models import *

class ShowUser(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_active', 'last_login']

class ShowAddressUser(admin.ModelAdmin):
    list_display = ['id', 'idUser', 'name', 'lastName', 'address', 'postalCode', 'town', 'province', 'country', 'phone']
    readonly_fields = ('id',)


admin.site.register(BasicUser, ShowUser)
admin.site.register(AddressUser, ShowAddressUser)


