from django.urls import include, path
from pedidos import views

urlpatterns = [

    path('', views.procesar_pedido, name='procesar_pedido'),
    
]