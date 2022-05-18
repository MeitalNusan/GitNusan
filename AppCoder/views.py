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
    if request.method =='POST':

        formulario=AnimalForm(request.POST)

        if formulario.is_valid():
            informacion=formulario.cleaned_data
            animal=Animal(nombre=informacion['nombre'], raza=informacion['raza'], edad=informacion['edad'])
            animal.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario=AnimalForm()
        return render(request, 'AppCoder/animales.html', {'formulario':formulario})

def jugadores(request):
    if request.method =='POST':

        formulario=JugadorForm(request.POST)

        if formulario.is_valid():
            informacion=formulario.cleaned_data
            jugador=Jugador(nombre=informacion['nombre'], equipo=informacion['equipo'], puesto=informacion['puesto'])
            jugador.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario=JugadorForm()
        return render(request, 'AppCoder/jugadores.html', {'formulario':formulario})

        
def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def busquedaRaza(request):
    return render(request,'AppCoder/busquedaRaza.html')

def buscar(request):
    if request.GET['raza']:
        raza=request.GET['raza']
        animales=Animal.objects.filter(raza=raza)
        return render(request, "AppCoder/resultadosBusqueda.html", {'raza': raza})
    else:
       respuesta= "No se ingreso ninguna raza"
       return HttpResponse(respuesta)
