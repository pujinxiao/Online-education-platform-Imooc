# -*- coding: utf-8 -*-
# 这里做一些类和类之间的继承

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))          # 如果检测到为登入状态会自动跳转到登录页面
    def dispatch(self, request, *args, **kwargs):                   # 其中的参数是必须这样写的
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)