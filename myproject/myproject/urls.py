from django.conf.urls import include, url
from django.contrib import admin
from myapp import views
from myapp import forms

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^person/$', views.person, name='person'),
    url(r'^admin/', admin.site.urls),
    url(r'^person/all$', views.all_person, name='index'),
    url(r'^person/phone_form$', views.new_phone, name='new_phone'),
    url(r'^person/(?P<person_id>[0-9]+)/$', views.member, name='member'),

    url(r'^person/(?P<person_id>[0-9]+)/create_phone/$', views.member, name='create_phone'),

    url(r'^person/new$', views.CreatePersonView.as_view(), name='person-new',),
]
