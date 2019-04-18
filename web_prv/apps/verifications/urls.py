#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xiaoge'
__mtime__ = '19-4-17'
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
from verifications import views


app_name = 'verifications'

urlpatterns = [
    path('image_codes/<uuid:image_code_id>/',views.ImageCode.as_view(),name='verifications'),

]