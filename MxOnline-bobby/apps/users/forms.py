# -*- coding: utf-8 -*-
__author__ = 'bobby'
__date__ = '2016/10/29 23:01'

# forms 是django自己提供的验证
from django import forms                     # 这种from是通过字段名一致来联系
from captcha.fields import CaptchaField

from .models import UserProfile              # 用module from 来做 上面的from


class LoginForm(forms.Form):                           # （登录的验证）这里做form的验证可以减少查询数据库的负担，更快的给用户错误提醒
    username = forms.CharField(required=True)          # 该字段是必须要有的
    password = forms.CharField(required=True, min_length=5)     # 最小长度的为5


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)             # （注册的验证）
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})   # error_messages自定义错误信息


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ModifyPwdForm(forms.Form):                       # 修改密码
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'gender', 'birday', 'address', 'mobile']

