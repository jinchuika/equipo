"""myproject URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^person/$', views.person, name='person'),
    url(r'^admin/', admin.site.urls),
    url(r'^person/all$', views.all_person, name='index'),
    url(r'^person/(?P<question_id>[0-9]+)/$', views.member, name='member'),
    url(r'^person/(?P<question_id>[0-9]+)/detail/$', views.detail, name='detail'),
]
