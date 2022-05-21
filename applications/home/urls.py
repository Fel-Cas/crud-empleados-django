from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import PruebaView,PruebaListView, ListarPrueba, CrearPrueba, ResumenFoundatonView, Home1View, Home2View, HomeView
urlpatterns = [
    path('home/', PruebaView.as_view()),
    path('lista/', PruebaListView.as_view()),
    path('lista_pruebas/',ListarPrueba.as_view()),
    path('crear_prueba/', CrearPrueba.as_view()),
    path('resumen/', ResumenFoundatonView.as_view(), name='resumen_foundation'),
    path('home1/', HomeView.as_view(), name="home1"),
    path('home2/', Home1View.as_view(), name="home2"),
    path('home3/', Home2View.as_view(), name="home3")
]
