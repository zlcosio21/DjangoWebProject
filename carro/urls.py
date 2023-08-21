from django.contrib import admin
from django.urls import include, path
from carro import views

app_name = "carro"

urlpatterns = [

    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('vaciar/<int:producto_id>/', views.vaciar_carro, name='vaciar'),

]