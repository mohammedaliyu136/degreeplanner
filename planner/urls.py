from planner import views
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^login_out/', views.logout_user, name='login'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^register/', views.register, name='register'),
    url(r'^enroll_profile/', views.enroll_profile, name='profile'),
    url(r'^indexx/', views.indexx, name='get_info'),
    url(r'^degree_req/', views.degree_req, name='free_elective_req'),
    url(r'^my_view/', views.my_view, name='my_view'),
    url(r'^show_schedule/', views.show_schedule, name='planner'),
    url(r'^search/', views.search, name='search')
]
