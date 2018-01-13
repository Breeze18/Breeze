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
    url(r'^events/register/$',views.event_register, name='event_register'),
    url(r'^accomodation/register/$', views.accom_register, name='accom_register'),
    url(r'^events/register2/$',views.event_register2, name='event_register2'),
    url(r'^accomodation/register2/$',views.accom_register2, name='accom_register2'),
    url(r'^events/(?P<category>\w+)/(?P<subcategory>\w+)/$', views.specificEventView, name='specificView'),
    url(r'^events/(?P<category>\w+)/$', views.specificEventView, name='specificView'),
    url(r'^pronights/', views.pronights, name='pronights'),
    url(r'^forgotPassMail/', views.forgotmail, name='forgotmail'),
    url(r'^forgotPassword/(?P<hashkey>\w+)', views.forgot, name='forgot'),
    url(r'^me/', views.profile, name='profile'),
    url(r'^login/', views.login1, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
]
