from django.contrib import admin
from users.models import *

class ShowUser(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'username', 'email', 'password', 'is_active', 'last_login']

admin.site.register(BasicUser, ShowUser)

