import datetime
from dateutil.relativedelta import *
from django import forms
from django.forms.extras import SelectDateWidget
from .models import BasicUser
from django.core.exceptions import ObjectDoesNotExist

today = datetime.datetime.today()
first = today - relativedelta(years=70)
last = today - relativedelta(years=1)


class BaseUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class BaseUserRegisterForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=SelectDateWidget(years=range(first.year, last.year))
    )
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = BasicUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
            'password_confirmation'
        )
        widgets = {
            'password': forms.PasswordInput(),
            'password_confirmation': forms.PasswordInput(),
        }

    def clean(self):
        print len(self.cleaned_data)
        if (
            'password' and 'password_confirmation' in self.cleaned_data
        ):
            password = self.cleaned_data['password']
            password_conf = self.cleaned_data['password_confirmation']
            if password_conf != password:
                raise forms.ValidationError('Password do not match.')
        return self.cleaned_data

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

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            #this raises an ObjectDoesNotExist exception
            #if it doesn't find a user with that username
            BasicUser.objects.get(username=username)
        #if username doesn't exist, this is good. We can create the username
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already used.')

