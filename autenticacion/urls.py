from django.contrib import admin
from django.urls import include, path
from autenticacion import views

urlpatterns = [
    path('', views.autenticacion, name='autenticacion'),
]