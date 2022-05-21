from dataclasses import fields
from pyexpat import model
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView, 
    DeleteView
)
from .forms import EmpleadoForm
from applications.departamentos.models import Departamento

#models
from .models import Persona

# Create your views here.

class InicioView(TemplateView):
    """
    Vista que carga la página de inicio
    """
    template_name='inicio.html'
    

# 1.- Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name='personas/list_all.html'
    #paginación de los resultados
    paginate_by=3
    ordering='id'

    def get_queryset(self) :
        word=self.request.GET.get('keyword','')
        return Persona.objects.filter(
            full_name__icontains=word
        )

class ListAllEmpleadosAdmin(ListView):
    template_name='personas/list_empleados.html'
    #paginación de los resultados
    paginate_by=10
    ordering='id'
    context_object_name='empleados'
    model=Persona


# 2.- Listar todos los empleados que pertenecen a un área de la empresa
class ListEmpleadosByArea(ListView):
    template_name='personas/list_by_area.html'
    context_object_name='empleados'
    def get_queryset(self):
        print(self.kwargs['departamento'])
        #Filtrar 
        lista=Persona.objects.filter(
            departamento__name=f"{self.kwargs['departamento']}"
        )
        return lista

# 3.- Listar empleados por trabajo
class ListEmpleadosByJob(ListView):
    template_name='personas/list_by_job.html'
    def get_queryset(self):
        print(self.kwargs['job'])
        #Filtrar 
        lista=Persona.objects.filter(
            job=self.kwargs['job']
        )
        return lista

# 4.- Listar los empleados por palabra clave
class ListEmpleadoByKeyWord(ListView):
    template_name='personas/list_by_word.html'
    context_object_name='empleados'
    def get_queryset(self) :
        print(self.request.GET.get('keyword',''))
        word=self.request.GET.get('keyword','')
        return Persona.objects.filter(
            name=word
        )
# 5.- Listar habilidades de un empleado
class ListHabilidadesEmpleados(ListView):
     template_name='personas/habilidades.html'
     context_object_name='habilidades'
     def queryset(self):
         empleado=Persona.objects.get(id=self.request.GET.get('empleado',))
         return empleado.habilidades.all()

# Detalle de un empleado
class EmpleadoDetailView(DetailView):
    model=Persona
    template_name='personas/detail_empleado.html'

    def get_context_data(self, **kwargs):
        context=super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context

class SuccesView(TemplateView):
    template_name='personas/success.html'

class CreateEmpleado(CreateView):
    model=Persona
    template_name='personas/add.html'
    form_class=EmpleadoForm
    """ fields=['name', 'lastName', 'job', 'departamento','habilidades', 'hoja_vida'] """
    success_url=reverse_lazy('empleados_app:empleados_admin')
    #Intercertar un form válido para generar un nuevo valor
    def form_valid(self, form):
        #lógica del proceso
        empleado=form.save(commit=False)#Para no guardar en la BD, solo crear la instancia
        empleado.full_name=f'{empleado.name} {empleado.lastName}'
        empleado.save()
        return  super(CreateEmpleado, self).form_valid(form)

class EmpleadoUpdate(UpdateView):
    template_name='personas/update.html'
    model=Persona
    fields=[
        'name',
        'lastName',
        'job',
        'departamento',
        'habilidades',
        'hoja_vida'
    ]
    success_url=reverse_lazy('empleados_app:empleados_admin')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #lógica del proceso
        empleado=form.save(commit=False)#Para no guardar en la BD, solo crear la instancia
        empleado.full_name=f'{empleado.name} {empleado.lastName}'
        empleado.save()
        return  super(EmpleadoUpdate, self).form_valid(form)

class DeleteEmpleado(DeleteView):
    template_name='personas/delete.html'
    model=Persona
    success_url=reverse_lazy('empleados_app:empleados_admin')
    