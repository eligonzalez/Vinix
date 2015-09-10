from django.contrib import admin
from socialNetwork.models import *

class ShowPost(admin.ModelAdmin):
    list_display = ['id', 'idUser1', 'idUser2', 'comment', 'date']

class ShowFollower(admin.ModelAdmin):
    list_display = ['id', 'idUser1', 'idUser2']

admin.site.register(Post, ShowPost)
admin.site.register(Follower, ShowFollower)