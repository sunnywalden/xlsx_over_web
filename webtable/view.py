# --*-- coding:utf8 --*--
import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm

from webtable.loadCsv.csvLloader import loader
from webtable.loadCsv.dataloader import getdata
from webtable.userManage.user_login import user_login
from webtable.userManage.user_registry import user_registry
from webtable.userManage.userlogout import userlogout
from webtable.models import User

uname = ''

def query(request):
    lists = getdata()
    return render(request, 'login/productiondashboard.html', {'lists': lists})

def home(request):
    lists = getdata()
    return render(request, 'login/productiondashboard.html', {'lists': lists})

def index(request):
    lists = getdata()
    return render(request, 'login/productiondashboard.html', {'lists': lists, 'username': uname})

def load(request):
    username = request.GET.get('username')
    res = loader('static/upload/LCD看板--生产块.xlsx')
    if res:
        print('username in load is:', username)
        return JsonResponse({'data': res})
    else:
        print('display xlsx file failed in load func')
        return JsonResponse(username, status=500)

@csrf_exempt
def userlogin(request):
    response = user_login(request)
    if response.status_code == 200:
        response_data = json.loads(response.content)
        uname = response_data.get('username')
        print('The user logging is:', uname)
        res = loader('static/upload/LCD看板--生产块.xlsx')
        if res:
            return JsonResponse({'lists': res, 'username': uname})
    else:
        print('username returned by user_login func is none')
        return response

def login(request):
    return render(request, "login/login.html")

@csrf_exempt
def userregistry(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    res = user_registry(request)
    print(res)
    if res:
        return redirect(reverse('userlogin'))
    else:
        return JsonResponse({'error': 'User registration failed'}, status=500)

def registry(request):
    return render(request, "login/register.html")

def userlogout(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == "POST":
        name = request.POST.get("username")
        print('Debug username in user logout:', name)
        User.objects.update(Username=name, LoginStatus=False)

        user = User.objects.filter(Username=name, LoginStatus=False)
        for u in user:
            print(u.Username, u.LoginStatus)
            if not u.LoginStatus:
                print('user', u.Username, 'logout success')
                return render(request, "login/login.html", context={'next': redirect_to})
