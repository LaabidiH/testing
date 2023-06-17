from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.Home, name="home"),
    path("actives",views.actives, name="actives"),
    path("contact",views.contact, name="contact"),
    path('signup/', views.signup, name='signup'),
    path('cons/', views.cons, name='cons'),
    path('archive/', views.archive_dossiers, name='archive_dossiers'),
    path('radio/', views.radio, name='radio'),
    path('bio/', views.bio, name='bio'),
    path('radiologie/', views.service_radio, name='service_radio'),
    path('biologie/', views.service_biologie, name='service_biologie'),
    path('radiologieL/', views.service_radioL, name='service_radioL'),
    path('biologieL/', views.service_biologieL, name='service_biologieL'),
]