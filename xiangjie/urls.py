"""xiangjie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from xiangjieapp.views import index,newsshow,newsshowall,questionshowall,questionshow
from xiangjieapp.views import product,danwendankong,shuangwenshuangkong,jiguikongtiao,hengwena,hengwenb,haixianji
from xiangjieapp.views import about,honor,contact
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from xiangjie.upload import upload_image

urlpatterns = [
    url(r'^$',index),
    url(r'^news/(\w+)$',newsshow),
    url(r'^new',newsshowall),
    url(r'^questions/(\w+)$', questionshow),
    url(r'^question', questionshowall),
    url(r'^product',product),
    url(r'^danwendankong',danwendankong),
    url(r'^shuangwenshuangkong',shuangwenshuangkong),
    url(r'^jiguikongtiao',jiguikongtiao),
    url(r'^hengwena',hengwena),
    url(r'^hengwenb',hengwenb),
    url(r'^haixianji',haixianji),
    url(r'^about',about),
    url(r'^honor',honor),
    url(r'^contact',contact),
    path('admin/', admin.site.urls),
    url(r'^admin/uploads/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r"^uploads/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT, }),
]