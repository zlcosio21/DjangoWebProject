from django.shortcuts import redirect
from .carro import Carro
from tienda.models import Producto

# Create your views here.
def agregar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto = producto)

    return redirect("tienda")


def eliminar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminar(producto=producto)

    return redirect("tienda")

def restar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.restar(producto = producto)

    return redirect("tienda")

def vaciar_carro(request, producto_id):

    carro = Carro(request)

    carro.vaciar_carro()

    return redirect("tienda")