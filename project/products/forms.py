from django import forms
from django.forms.extras import SelectDateWidget
from django.core.exceptions import ObjectDoesNotExist
import datetime
from dateutil.relativedelta import *
from .models import Product

class addProduct(forms.Form):
    amount = forms.IntegerField()
    idProd = forms.CharField()

class searchForm(forms.Form):
    word = forms.CharField()

class addCommentProduct(forms.Form):
    comment = forms.CharField()
    idProduct = forms.CharField()
    punctuation = forms.CharField()
