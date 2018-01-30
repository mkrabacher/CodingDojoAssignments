from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<number>\d+)$', views.student),
    url(r'^classes/(?P<number>\d+)$', views.classes),
    url(r'^classes/$', views.classesPage),
    url(r'^createClass/$', views.createClass),
    url(r'^enrollClass/$', views.enrollClass),
    url(r'^cancelClass/$', views.cancelClass),
    url(r'^createRating/$', views.createRating),
    url(r'^createRating/$', views.createRating),
    url(r'^timeForm/$', views.timeForm),
    url(r'^timeSubmit/$', views.timeSubmit),
]
