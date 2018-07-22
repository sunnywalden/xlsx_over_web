# --*-- coding:utf8 --*--
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from webtable.loadCsv.csvLloader import loader
from webtable.loadCsv.dataloader import getdata, show

from webtable.userManage.user_login import user_login
from webtable.userManage.user_registry import user_registry
from webtable.userManage.userlogout import userlogout
from django.views.decorators.csrf import csrf_exempt
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
    res = loader('static/upload/LCD看板--生产块.xlsx')
    if res:
        #index(request)
        #print('debug in view.load:', res)
        print('username in load is:', uname)
        return render(request, 'login/productiondashboard.html', {'lists': res, 'username': uname})

# def hello(request):
#     return HttpResponse("Hello world ! ")
@csrf_exempt
def userlogin(request):
#    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    global uname
    uname = user_login(request)

    if uname:
        print('The user logging is:', uname)
#        return render(request, 'login/productiondashboard.html')
#        return HttpResponseRedirect('login/productiondashboard.html')
#        return HttpResponseRedirect(load(request))
        res = loader('static/upload/LCD看板--生产块.xlsx')
        if res:
#            return redirect(redirect_to)
            return render(request, 'login/productiondashboard.html', {'lists': res, 'username': uname})
#            return render(request, "login/productiondashboard.html", context={'lists': res, 'username': uname, 'next': redirect_to})
    else:
        print('username returned by user_login func is none')
        return render(request, "login/login.html")
#    return render(request, 'login/productiondashboard.html', {'lists': res, 'username': uname})

def login(request):

#    res = userlogin(request)
#    if res:
#        return render(request, 'login/productiondashboard.html')
#    else:
        return render(request, "login/login.html")

@csrf_exempt
def userregistry(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    res = user_registry(request)
    print(res)
    if res:
#        return redirect(redirect_to)
#        return HttpResponseRedirect("login/login.html")
        return render(request, "login/login.html", context={'next': redirect_to})
    else:
        return render(request, "login/register.html")


def registry(request):
    return render(request, "login/register.html")
#    else:
#        return render_to_response("login/register.html")
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         new_user = form.save()
    #         return HttpResponseRedirect("login/login.html")
    # else:
    #     form = UserCreationForm()
    # return render_to_response("login/register.html", {
    #     'form': form,
    # })


def userlogout(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == "POST":
        name = request.POST.get("username")
        print('Debug username in user logout:', name)
#        User.objects.filter(Username=name)
        User.objects.update(Username=name, LoginStatus=False)

        user = User.objects.filter(Username=name, LoginStatus=False)
        for u in user:
            print(u.Username, u.LoginStatus)
            if not u.LoginStatus:
                print('user', u.Username, 'logout success')
#                return render_to_response("login/login.html")
#                return HttpResponseRedirect('login')
                return render(request, "login/login.html", context={'next': redirect_to})
