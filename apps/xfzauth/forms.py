#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from django import forms
from apps.froms_erros import FormMixin


class LoginForm(forms.Form, FormMixin):
    telephone = forms.CharField(max_length=11, error_messages={"max_length": "密码不能超过11位"})
    remember = forms.IntegerField(required=False, )
    password = forms.CharField(max_length=11, min_length=6,
                               error_messages={"max_length": "密码不能超过11位", "min_length": "密码必须超过6位"})
