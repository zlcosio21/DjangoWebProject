from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):

    return render(request, "DjangoWebApp/home.html")


def servicios(request):

    return render(request, "DjangoWebApp/servicios.html")


def tienda(request):

    return render(request, "DjangoWebApp/tienda.html")


def blog(request):

    return render(request, "DjangoWebApp/blog.html")


def contacto(request):

    return render(request, "DjangoWebApp/contacto.html")