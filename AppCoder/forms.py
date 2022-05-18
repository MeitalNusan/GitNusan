from django import forms

class PersonaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    edad=forms.IntegerField()

class AnimalForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    raza=forms.CharField(max_length=50)
    edad=forms.IntegerField()


class JugadorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    equipo=forms.CharField(max_length=50)
    puesto=forms.CharField(max_length=50)
    



    

