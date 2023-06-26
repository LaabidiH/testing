from django.urls import path, include
from . import views

from testme.views import generate_pdf
from testme.views import liste_dossiers_patients
from testme.views import generate_pdf_pris

urlpatterns = [
    path("home/",views.Home, name="home"),
    path("actives",views.actives, name="actives"),
    path("contact",views.contact, name="contact"),
    path('signup/', views.signup, name='signup'),
    path('cons/', views.cons, name='cons'),
    path('archive/', views.archive_dossiers, name='archive_dossiers'),
    path('radio/', views.radio, name='radio'),
    path('bio/', views.bio, name='bio'),
    path('saa/', views.saa, name='saa'),
    path('saa2/', views.saa2, name='saa2'),

    ##############
    path('home_M/', views.home_M, name="home_M"),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),
    path('scan_M/', views.scan_M, name='scan_M'),
    path('prischarge/', views.prischarge, name='prischarge'),
    path('contact_M/', views.contact_M, name='contact_M'),
    path('archive_CH/', views.archive_CH, name='archive_CH'),
    path('archive_P/', views.archive_P, name='archive_P'),
    path('dossiers/', liste_dossiers_patients, name='liste_dossiers_patients'),
    path('generate-pdf_pris/', generate_pdf_pris, name='generate_pdf_pris'),
    path('home2/', views.Home2, name='home2'),
    path('user_login/', views.user_login, name='user_login'),
]