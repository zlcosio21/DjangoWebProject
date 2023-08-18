from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
import os
from dotenv import load_dotenv

# Email and password private
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Create your views here.
def contacto(request):

    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde DjangoWebProject", "El usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {} ".format(nombre, email, contenido), "",[EMAIL], reply_to=[email])

            try:
                email.send() 
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {"formulario":formulario_contacto})