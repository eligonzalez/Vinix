from django.contrib import admin
from socialNetwork.models import *

class ShowPost(admin.ModelAdmin):
    list_display = ['id', 'idUser', 'comment']

admin.site.register(Post, ShowPost)