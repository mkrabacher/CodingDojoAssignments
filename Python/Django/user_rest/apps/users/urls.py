from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^newUser', views.newUser),
    url(r'^createUser', views.createUser),
    url(r'^update', views.update),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/destroy$', views.destroy)
]