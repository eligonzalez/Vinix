from django.db import models
from .models import *
from users.models import BasicUser
import datetime

class Post(models.Model):
    idUser1 = models.ForeignKey(BasicUser, null=False, related_name='writer', default=None)
    idUser2 = models.ForeignKey(BasicUser, null=False, related_name='receiver', default=None)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.id)

class Follower(models.Model):
    idUser1 = models.ForeignKey(BasicUser, null=False, related_name='follower')
    idUser2 = models.ForeignKey(BasicUser, null=False, related_name='followed')
    def __str__(self):
        return str(self.id)