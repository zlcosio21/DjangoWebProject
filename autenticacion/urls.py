from django.contrib import admin
from django.urls import include, path
from .views import VistaRegistro

urlpatterns = [
    path('', VistaRegistro.as_view(), name='autenticacion'),
]