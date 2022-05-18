from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('personas/', personas, name='personas'),
    path('animales/', animales, name= 'animales'),
    path('jugadores/',jugadores, name='jugadores'),
    
]