#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_POST
from .forms import LoginForm
from utils import restful


@require_POST
def login_views(request):
    forms = LoginForm(request.POST)
    if forms.is_valid():
        telephone = forms.cleaned_data.get('telephone')
        password = forms.cleaned_data.get('password')
        remember = forms.cleaned_data.get('remember')
        print(remember)
        user = authenticate(request, username=telephone, password=password)
        if user:
            if user.is_active:
                # 登陆
                login(request, user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful.ok()
            else:
                return restful.unauth(message='您的账号已被冻结!')
        else:
            return restful.param_error(message="手机或账号密码错误！")
    else:
        errors = forms.get_errors()
        return restful.param_error(message=errors)


def logout_view(request):
    logout(request)
