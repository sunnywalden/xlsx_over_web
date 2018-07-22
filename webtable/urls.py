# --*-- coding:utf8 --*--
"""webtable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import view

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', view.login),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),
    url(r'^query$', view.query),
    path(r'loader/', view.load),
    url(r'^index/$', view.index),
    url(r'^$', view.login),
    path(r'userlogin/',  view.userlogin),
    url(r'^userregistry$',  view.userregistry),
    url(r'^registry$',  view.registry),
    url(r'^login',  view.login),
    url(r'^userlogout/$',  view.login),
    url(r'userlogout/',  view.userlogout),

]


