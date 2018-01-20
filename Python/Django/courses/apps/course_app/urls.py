from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^addCourse$', views.addCourse),
    url(r'^createCourse$', views.createCourse),
    url(r'^removeCourse$', views.removeCourse),
    url(r'^remove/(?P<number>\d+)$', views.remove)
]
