from django.contrib import admin
from django.urls import include, path
from .views import VistaRegistro, cerrar_sesion, iniciar_sesion

urlpatterns = [

    path('', VistaRegistro.as_view(), name='autenticacion'),
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),

]