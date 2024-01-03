from django.contrib import admin
from django.urls import path,include
from Home import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("Home",views.index,name='Home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("cafe",views.cafe,name='cafe'),
    path("contact",views.contact,name='contact')
]