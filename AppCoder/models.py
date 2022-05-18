from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    
    def __str__(self):
        return self.nombre + " " + str(self.edad) 

class Animal(models.Model):
    nombre=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    edad=models.IntegerField()
    
    def __str__(self):
        return self.nombre + " " + self.raza + str(self.edad)

class Jugador(models.Model):
    nombre=models.CharField(max_length=50)
    equipo=models.CharField(max_length=50)
    puesto=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.equipo + self.puesto

    

