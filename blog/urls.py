from django.contrib import admin
from django.urls import include, path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
]