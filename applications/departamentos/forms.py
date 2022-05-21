from django import forms

class NewDepartamentoForm(forms.Form):
    name=forms.CharField(max_length=50)
    last_names=forms.CharField(max_length=50)
    departamento=forms.CharField(max_length=50)
    shortname=forms.CharField(max_length=50)

