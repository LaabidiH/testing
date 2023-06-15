from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.Home, name="home"),
    path("actives",views.actives, name="actives"),
    path("contact",views.contact, name="contact"),
    path('archive/', views.archive_dossiers, name='archive_dossiers'),
]