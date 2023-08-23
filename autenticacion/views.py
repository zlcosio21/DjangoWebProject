from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.
class VistaRegistro(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})

    def post(self, request): 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home') 
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render(request, "registro/registro.html", {"form":form})
        
def iniciar_sesion(request):
    form = AuthenticationForm()
    return render(request, "iniciar_sesion/iniciar_sesion.html", {"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')