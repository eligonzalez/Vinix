from django.db import models
from datetime import date
from django.contrib.auth.models import User


class BasicUser(User):
    dni = models.CharField(max_length=12, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return str(self.id)
    def age(self):
        days_in_year = 365.2425
        return int((date.today() - self.birth_date).days / days_in_year)

    @classmethod
    def set_BasicUser(self, client, cl):
        client.username = cl.cleaned_data["email"]
        client.first_name = cl.cleaned_data["first_name"]
        client.last_name = cl.cleaned_data["last_name"]
        client.email = cl.cleaned_data["email"]
        password1 = cl.cleaned_data["password1"]
        password2 = cl.cleaned_data["password2"]
        if password1 == password2 :
            client.set_password(cl.cleaned_data["password1"])
            return 0
        else :
            return 1
        client.save()

class AddressUser(models.Model):
    idUser = models.ForeignKey(BasicUser)
    name = models.CharField(max_length=50, blank=True, null=True)
    lastName =  models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    postalCode = models.CharField(max_length=5, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    addressDefault = models.BooleanField(default=True, blank=True)
    country = models.CharField(max_length=50, default='España', blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name

    @classmethod
    def set_AddressUser(self,user,cd):
        exists = AddressUser.objects.filter(idUser=user.id).exists()

        if exists :
            ad = AddressUser.objects.get(idUser=user.id)
        else :
            ad = AddressUser()
            ad.idUser = BasicUser.objects.get(id=user.id)

        ad.address = cd.cleaned_data["address"]
        ad.province = cd.cleaned_data["province"]
        ad.town = cd.cleaned_data["town"]
        ad.country = cd.cleaned_data["country"]
        ad.postalCode = cd.cleaned_data["postalCode"]
        ad.phone = cd.cleaned_data["phone"]
        ad.save()

