from webtable.models import User

from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import HttpResponseRedirect


def userlogout(username):
    res = User.objects.filter(Username=username)
    if res:
        User.objects.update(LoginStatus=False)
        return HttpResponseRedirect('login/login.html')
    else:
        return False
