from django.urls import path, include
from . import views

urlpatterns = [
    path("home",views.Home, name="home"),
    path("actives",views.actives, name="actives"),
    path("contact",views.contact, name="contact"),
    path('signup/', views.signup, name='signup'),
    path('cons/', views.cons, name='cons'),
    path('archive/', views.archive_dossiers, name='archive_dossiers'),
    path('radio/', views.radio, name='radio'),
    path('bio/', views.bio, name='bio'),
    path('saa/', views.saa, name='saa'),
    path('saa2/', views.saa2, name='saa2'),
]