from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from users.models import *
from django.shortcuts import get_object_or_404
from django.template import RequestContext


def home_social(request):
    users = BasicUser.objects.all()
    return render(request, 'home_social.html', {'users': users})

