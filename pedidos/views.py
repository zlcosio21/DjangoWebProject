from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, LineaPedido
from carro.carro import Carro
from django.contrib import messages

# Create your views here.
@login_required(login_url = "autenticacion/iniciar_seson")
def procesar_pedido(request):
    
    pedido = Pedido.objects.create(user = request.user)
    carro = Carro(request)

    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido

        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    messages.success(request, "El pedido ha sido un exito")