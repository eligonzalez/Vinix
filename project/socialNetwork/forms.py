from django import forms
from django.forms.extras import SelectDateWidget
from django.core.exceptions import ObjectDoesNotExist
import datetime
from dateutil.relativedelta import *
from .models import Post


class addPostForm(forms.Form):
    post = forms.CharField()
