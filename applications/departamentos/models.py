from django.db import models

# Create your models here.
class Departamento(models.Model):
    name=models.CharField('name', max_length=100)
    short_name=models.CharField('shortName', max_length=20, unique=True)
    anulate=models.BooleanField('anulate', default=False)    

    class Meta:
        verbose_name='Mi departamento'
        verbose_name_plural='Areas de la empresa'
        ordering=['name'] ## para orden inverso usamos guión (-)
        unique_together=('name', 'short_name')

    def __str__(self) -> str:
        return self.name+'-'+self.short_name