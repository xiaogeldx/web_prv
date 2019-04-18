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
from django.urls import path, re_path
from doc import views

app_name = 'doc'

urlpatterns = [
    path('docDownload/',views.docDownload,name='docDownload'),
]