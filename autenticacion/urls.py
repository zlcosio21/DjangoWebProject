from django.contrib import admin
from django.urls import include, path
from .views import VistaRegistro, cerrar_sesion

urlpatterns = [

    path('', VistaRegistro.as_view(), name='autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),

]