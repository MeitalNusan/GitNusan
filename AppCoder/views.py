from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import *
from AppCoder.forms import *

def personas(request):
    if request.method =='POST':
        formulario=PersonaForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            persona=Persona(nombre=informacion['nombre'], edad=informacion['edad'])
            persona.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario=PersonaForm()
        return render(request, 'AppCoder/personas.html', {'formulario':formulario})

def animales(request):
    return render(request, 'AppCoder/animales.html')

def jugadores(request):
    return render(request, 'AppCoder/jugadores.html')

def inicio(request):
    return render(request, 'AppCoder/inicio.html')
