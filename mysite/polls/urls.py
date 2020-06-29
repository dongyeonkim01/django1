from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('t1', views.index, name ='index'),
    url(r'^upload/$', views.upload),

]