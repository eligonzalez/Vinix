from django import forms
from django.forms.extras import SelectDateWidget
from django.core.exceptions import ObjectDoesNotExist
import datetime
from dateutil.relativedelta import *
from .models import Post
from users.models import *


class addPostForm(forms.Form):
    post = forms.CharField()
    receiver=forms.IntegerField()

class UploadFileForm(forms.Form):
    image = forms.ImageField()