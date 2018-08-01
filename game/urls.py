#if you go to this URL, it shows you this view

from django.urls import path
from django.conf.urls import url

from . import views

#if someone types nothing, they'll go to the index view
app_name = 'game'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^game/$', views.game, name='game'),
]
