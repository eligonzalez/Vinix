from django.db import models
from .models import *
from users.models import BasicUser
import datetime

class Post(models.Model):
    idUser = models.ForeignKey(BasicUser)
    comment = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.id)