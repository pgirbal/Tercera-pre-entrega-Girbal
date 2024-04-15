from django.db import models

# Create your models here.

class Practica(models.Model):

    nombre = models.CharField(max_length=40)
    asignatura = models.CharField(max_length=30)
    fecha = models.DateField()

class Docente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    legajo = models.IntegerField()
    email = models.EmailField()

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
