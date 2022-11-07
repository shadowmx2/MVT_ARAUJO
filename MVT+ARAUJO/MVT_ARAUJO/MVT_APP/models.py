from django.db import models

# Create your models here.

 

class Familia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=100)
    dni = models.IntegerField()
    fechaNacimiento = models.DateField()

 