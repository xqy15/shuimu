"""shuimu URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import shuimu.app.views as views
from django.contrib.staticfiles.urls import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^aboutus$', views.aboutus, name='aboutus'),
    url(r'^test$', views.test, name='test'),
    url(r'^page1/$', views.page1, name='page1'),
    url(r'^page3/$', views.page3, name='page3'),
    url(r'^page5/$', views.page5, name='page5'),
    url(r'^page7/$', views.page7, name='page7'),
]
