from django.db import models
from datetime import date
from django.contrib.auth.models import User


class BasicUser(User):
    dni = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return str(self.id)
    def age(self):
        days_in_year = 365.2425
        return int((date.today() - self.birth_date).days / days_in_year)

class AddressUser(models.Model):
	idUser = models.ForeignKey(BasicUser)
	name = models.CharField(max_length=50, blank=True)
	lastName =  models.CharField(max_length=50, blank=True)
	address = models.CharField(max_length=50, blank=True)
	postalCode = models.CharField(max_length=5, blank=True)
	town = models.CharField(max_length=50, blank=True)
	province = models.CharField(max_length=50, blank=True)
	addressDefault = models.BooleanField(default=False, blank=True)
	country = models.CharField(max_length=50, default='España', blank=True)
	phone = models.CharField(max_length=50, blank=True)
	def __str__(self):
		return self.name
