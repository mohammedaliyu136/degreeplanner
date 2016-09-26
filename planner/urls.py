from planner import views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^header/', views.header, name='header'),
]