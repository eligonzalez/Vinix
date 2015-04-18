from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class BasicUser(User):
    dni = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def age(self):
        days_in_year = 365.2425
        return int((date.today() - self.birth_date).days / days_in_year)

