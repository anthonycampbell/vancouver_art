from django.conf.urls import patterns, url
from art_map import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'))
