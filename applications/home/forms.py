from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):

    class Meta:
        model=Prueba
        fields=(
            'title',
            'content',
            'cantidad'
        )
        widgets={
            'cantidad': forms.NumberInput(
                attrs={
                    'placeholder':'Ingrese la cantidad'
                }
            ),
            'title':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese el titulo de la prueba'
                }
            )

        }
    
    def clean_cantidad(self):
        cantidad=self.cleaned_data['cantidad']
        if cantidad<10 or cantidad>20:
            raise forms.ValidationError('Ingrese un valor entre 10 y 20')
        return cantidad
