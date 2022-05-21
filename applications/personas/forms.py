from dataclasses import fields
from django import forms
from .models import Persona

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Persona
        fields=(
        'name',
        'lastName',
        'job',
        'departamento',
        'habilidades',
        'hoja_vida', 
        'avatar'
        )
        widgets={
            'habilidades': forms.CheckboxSelectMultiple()
        }