from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<contact_id>[0-9]+)/$', views.contact_detail, name='detail'),
    url(r'^(?P<contact_id>[0-9]+)/edit', views.create_contact, name='create_contact'),
    url(r'^new', views.new_contact, name='new_contact'),
    url(r'^donate', views.new_donation, name='new_donation'),

    url(r'^r$', views.meeting_index, name='meeting_index'),
    url(r'^r/new', views.new_meeting, name='new_meeting'),
    url(r'^r/(?P<meeting_id>[0-9]+)/$', views.meeting_detail, name='meeting_detail'),
    url(r'^r/(?P<meeting_id>[0-9]+)/edit$', views.meeting_edit, name='meeting_edit'),
]
