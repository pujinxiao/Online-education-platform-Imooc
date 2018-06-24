# _*_ encoding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView    # 处理的文件是静态文件
import xadmin
from django.views.static import serve     # 处理静态文件

from users.views import LogoutView, LoginView, RegisterView, AciveUserView, ForgetPwdView, ResetView, ModifyPwdView # 在views中定义的类都可以导进来，调用as_view() 传进来句柄

from users.views import IndexView
from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT
# from MxOnline.settings import STATIC_ROOT   # 如果是在真实环境下就要去掉这个注释

# 想要改网址的时候，修改 urls.py 中的正则表达式部分（url 参数第一部分），name 不变的前提下，其它地方都不需要修改。
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name="index"),                     # 端口后面什么都不加 就会加载index页面
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),                       # 验证码的链接，如果是captcha/开头的链接，都会路由到captcha.urls的配置的url中
    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_active"),   # (?P<active_code>.*)/$ 提取变量值
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace="org")),      # 命名空间 防止organization下的url和主目录下的url 有冲突，，，有了namespace="org" 他只会去org下找

    # 课程相关url配置
    url(r'^course/', include('courses.urls', namespace="course")),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$',  serve, {"document_root":STATIC_ROOT}),    # 如果是在真实环境下就要去掉这个注释

    # 课程相关url配置
    url(r'^users/', include('users.urls', namespace="users")),

    # 富文本相关url
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]

# 全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'