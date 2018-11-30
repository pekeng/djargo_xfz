#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.urls import path
from apps.news import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='news'),
    path('<int:news_id>/', views.news_detail, name='news_detail'),
    path('search/', views.search, name='search')
]
