from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^billing', views.billing),
    url(r'^checkout', views.checkout)
]