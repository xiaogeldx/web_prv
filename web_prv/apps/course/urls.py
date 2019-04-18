#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xiaoge'
__mtime__ = '19-4-15'
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
from course import views
from django.urls import path, re_path

app_name = 'course'

urlpatterns = [
    path('course/',views.course,name='course'),
    path('course_detail/',views.course_detail,name='course_detail'),

]