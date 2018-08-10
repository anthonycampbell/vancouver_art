from django.conf.urls import patterns, url
from art_map import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'), 
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^add_favourite/$', views.add_favourite, name='add_favourite'),
    url(r'^profile/$', views.profile, name='profile'),)
