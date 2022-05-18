from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import *

def personas(request):
    return render(request, 'AppCoder/personas.html')

def animales(request):
    return render(request, 'AppCoder/animales.html')

def jugadores(request):
    return render(request, 'AppCoder/jugadores.html')

def inicio(request):
    return render(request, 'AppCoder/inicio.html')
