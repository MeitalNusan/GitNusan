from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    

class Animal(models.Model):
    nombre=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    edad=models.IntegerField()
    

    def __str__(self):
     return self.nombre + " " + str(self.edad) + self.raza

class Jugador(models.Model):
    nombre=models.CharField(max_length=50)
    equipo=models.CharField(max_length=50)
    puesto=models.CharField(max_length=50)
    

