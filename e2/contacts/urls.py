from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<contact_id>[0-9]+)/$', views.contact_detail, name='detail'),
    url(r'^(?P<contact_id>[0-9]+)/edit', views.create_contact, name='create_contact'),
    url(r'^new', views.new_contact, name='new_contact'),
]
