# --*-- coding:utf8 --*--
from django.http import HttpResponse
from django.shortcuts import render

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from webtable.loadCsv.csvLloader import loader
from webtable.loadCsv.dataloader import getdata, show


def query(request):
    lists = getdata()
    return render(request, 'login/productiondashboard.html', {'lists': lists})


def home(request):
    lists = getdata()
    return render(request, 'login/productiondashboard.html', {'lists': lists})


def index(request):
    lists = getdata()
    return render(request, 'login/productiondashboard.html', {'lists': lists})


def load(request):
    res = loader('static/upload/LCD看板--生产块.xlsx')
    if res:
        #index(request)
        #print('debug in view.load:', res)
        return render(request, 'login/productiondashboard.html', {'lists': res})

# def hello(request):
#     return HttpResponse("Hello world ! ")


def login(request):
    return render(request, 'login/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("index.html")
    else:
        form = UserCreationForm()
    return render_to_response("login/register.html", {
        'form': form,
    })