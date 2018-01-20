
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registerUser$', views.registerUser),
    url(r'^login$', views.login),
    url(r'^success$', views.success)
]
