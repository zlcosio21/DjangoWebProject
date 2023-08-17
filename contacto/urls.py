from django.contrib import admin
from django.urls import include, path
from contacto import views

urlpatterns = [
    path('', views.contacto, name='contacto'),
]