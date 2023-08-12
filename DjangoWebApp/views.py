from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.
def home(request):

    return render(request, "DjangoWebApp/home.html")


def servicios(request):

    servicios = Servicio.objects.all()

    return render(request, "DjangoWebApp/servicios.html", {"servicios":servicios})


def tienda(request):

    return render(request, "DjangoWebApp/tienda.html")


def blog(request):

    return render(request, "DjangoWebApp/blog.html")


def contacto(request):

    return render(request, "DjangoWebApp/contacto.html")