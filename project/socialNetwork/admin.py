from django.contrib import admin
from socialNetwork.models import *

class ShowPost(admin.ModelAdmin):
    list_display = ['id', 'idUser1', 'idUser2', 'comment', 'date']
    readonly_fields = ('date', 'id')

class ShowFollower(admin.ModelAdmin):
    list_display = ['id', 'idUser1', 'idUser2']
    readonly_fields = ('id',)

admin.site.register(Post, ShowPost)
admin.site.register(Follower, ShowFollower)