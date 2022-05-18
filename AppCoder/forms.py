from django import forms

class PersonaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    

