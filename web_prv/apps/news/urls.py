#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xiaoge'
__mtime__ = '19-4-12'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━━━━┛┻┓
            ┃        ☃ ┃
            ┃  ┳┛ ┗┳   ┃
            ┃    ┻     ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━┓
              ┃ 神兽保佑  ┣┓
              ┃永无BUG！┏┛
              ┗┓┓┏━┳┓┏┛
              ┃┫┫  ┃┫┫
             ┗┻┛  ┗┻┛
"""
from django.urls import path, re_path
from news import views

app_name = 'news'
urlpatterns = [
    path('',views.index,name='index'),
    path('news_detail/',views.news_detail,name='news_detail'),
    path('search/',views.search,name='search'),

]
