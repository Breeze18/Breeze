from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sponsor/$', views.sponsor, name='sponsor'),
    url(r'^hospitality/$', views.hospitality, name='hospitality'),
    url(r'^transport/$', views.transport, name='transport'),
    url(r'^accomodation/$', views.accomodation, name='accomodation'),
    url(r'^events/technical/$',views.technical, name='technical'),
    url(r'^events/sports/$',views.sports, name='sports'),
    url(r'^events/cultural/$',views.cultural, name='cultural'),

    url(r'^events/(?P<category>\w+)/(?P<subcategory>\w+)/$', views.specificEventView, name='specificView'),
    url(r'^events/(?P<category>\w+)/$', views.specificEventView, name='specificView'),
]
