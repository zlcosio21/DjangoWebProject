from django.contrib import admin
from django.urls import include, path
from tienda import views

urlpatterns = [
    path('', views.tienda, name='tienda'),
]