from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.personas.models import Persona
from applications.departamentos.models import Departamento
# Create your views here.

class DepartmanetosList(ListView):
    template_name='departamento/lista.html'
    model= Departamento
    context_object_name='departamentos'

class NewDepartamentoView(FormView):
    template_name='departamento/new_departamento.html'
    form_class= NewDepartamentoForm
    success_url='/'

    def form_valid(self, form):
        name=form.cleaned_data['name']
        lastName=form.cleaned_data['last_names']
        depa=Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname']
        )
        depa.save()
        Persona.objects.create(
            name=name,
            lastName=lastName,
            full_name=f'{name} {lastName}',
            job=1,
            departamento=depa,
            hoja_vida='Es un buen empleado'
        )
        return super(NewDepartamentoView, self).form_valid(form)
