from django import forms
from django.forms.extras import SelectDateWidget
from django.core.exceptions import ObjectDoesNotExist
import datetime
from dateutil.relativedelta import *
from .models import Product


class finishPurchase_Form(forms.Form):
    name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    postal_code = forms.CharField(required=True)
    town = forms.CharField(required=True)
    country = forms.CharField(required=True)
    phone = forms.CharField(required=True)
