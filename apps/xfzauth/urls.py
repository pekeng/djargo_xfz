#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.urls import path
from apps.xfzauth import views

app_name = 'xfzauth'

urlpatterns = [
    path('login/', views.login_views, name='login')
]
