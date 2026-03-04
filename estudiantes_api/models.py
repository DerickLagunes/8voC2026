from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField()
    carrera = models.CharField(max_length=100)
    promedio = models.FloatField()

    def estudiar(self):
        pass

    def inscribirse(self):
        pass

    def __str__(self):
        return self.nombre
