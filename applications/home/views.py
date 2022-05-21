from email import contentmanager
from multiprocessing import context
from pyexpat import model
from re import template
from turtle import title
from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)
from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class PruebaView(TemplateView):
    template_name='home/prueba.html'

class ResumenFoundatonView(TemplateView):
    template_name='home/resumen_foundation.html'


class PruebaListView(ListView):
    template_name='home/lista.html'
    context_object_name='listaNumeros'
    queryset=[0, 12,45,78]
    
    
class ListarPrueba(ListView):
    template_name='home/lista_prueba.html'
    model=Prueba
    context_object_name='pruebas'

class CrearPrueba(CreateView):
    template_name='home/add.html'
    model=Prueba
    form_class=PruebaForm
    success_url='/'


class HomeView(TemplateView):
    template_name='home/home1.html'

class Home1View(TemplateView):
    template_name='home/home2.html'

class Home2View(TemplateView):
    template_name='home/home3.html'
