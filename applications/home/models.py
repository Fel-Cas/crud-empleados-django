from turtle import title
from django.db import models

class Prueba(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=200)
    cantidad=models.IntegerField()

    def __str__(self):
        return self.title + '-'+ self.content