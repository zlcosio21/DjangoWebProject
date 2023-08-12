from django.contrib import admin
from django.urls import include, path
from servicios import views

urlpatterns = [
    path('', views.servicios, name='servicios'),
]