from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.main ,name="main"),
    path('t1', views.index, name ='index'),
    url(r'^upload/$', views.upload),
    path('li',views.listview, name='list'),
]