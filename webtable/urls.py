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
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', view.login),
    re_path(r'^accounts/login/$', LoginView.as_view(), name='login'),
    re_path(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^query$', view.query, name='query'),
    path('loader/', view.load),
    re_path(r'^index/$', view.index, name='index'),
    re_path(r'^$', view.login, name='login'),
    path('userlogin/', view.userlogin),
    re_path(r'^userlogin$', view.userlogin, name='userlogin'),
    re_path(r'^userregistry$', view.userregistry, name='userregistry'),
    re_path(r'^registry$', view.registry, name='registry'),
    re_path(r'^login', view.login, name='login'),
    re_path(r'^userlogout/$', view.userlogout, name='userlogout'),
    re_path(r'userlogout/', view.userlogout, name='userlogout'),
]