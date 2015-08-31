from django import forms
from django.forms.extras import SelectDateWidget
from django.core.exceptions import ObjectDoesNotExist
import datetime
from dateutil.relativedelta import *
from .models import Product


class finishPurchase_Form(forms.Form):
    name = forms.CharField()
