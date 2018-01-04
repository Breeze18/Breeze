from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sponsor/', views.sponsor, name='sponsor'),
    url(r'^hospitality/', views.hospitality, name='hospitality'),
    url(r'^transport/', views.transport, name='transport'),
    url(r'^accomodation/', views.accomodation, name='accomodation'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
]
