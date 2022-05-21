from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from typing import Hashable
from django.db import models
from applications.departamentos.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Hablidades(models.Model):
    habilidad=models.CharField('Habilidad', max_length=100)
    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades de los empleados'

    def __str__(self) -> str:
        return str(self.id)+' - '+ self.habilidad


class Persona(models.Model):
    """Modelo para tabla empleados"""

    job_choices=(
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )

    name=models.CharField('Nombres',max_length=60)
    lastName=models.CharField('Apellidos',max_length=60)
    full_name=models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    #Contados
    #Administrador
    #Economista
    job=models.CharField('Trabajo',max_length=50, choices=job_choices)
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_lenght=None )
    habilidades=models.ManyToManyField(Hablidades)
    hoja_vida= RichTextField()
    avatar=models.ImageField(upload_to='empleado', blank=True, null=True)
    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados de la empresa'
        ordering=['name', 'lastName']

    def __str__(self) -> str:
        return str(self.id)+'-'+self.name+'-'+self.lastName

