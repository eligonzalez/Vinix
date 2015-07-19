#Django Imports
from django import forms
from django.forms.extras import SelectDateWidget
from django.core.exceptions import ObjectDoesNotExist
#Util Imports
import datetime
from dateutil.relativedelta import *
#Project Imports
from .models import BasicUser



today = datetime.datetime.today()
first = today - relativedelta(years=70)
last = today - relativedelta(years=1)


class BasicUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class BasicUserRegisterForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    class Meta():
        model = BasicUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
        )



    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            #this raises an ObjectDoesNotExist exception
            #if it doesn't find a user with that email
            BasicUser.objects.get(email=email)
        #if email doesn't exist, this is good. We can create the email
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('Email is already used.')

class edit_account_form(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField()
    province = forms.CharField()
    country = forms.CharField()
    postalCode = forms.CharField()
    phone = forms.CharField()


