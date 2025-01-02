# Create your models here.
from django.db import models

class Clase1(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Clase2(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()

class Clase3(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
from django.db import models

class Clase1(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Clase2(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()

class Clase3(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
