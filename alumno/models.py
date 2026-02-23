from django.db import models

# Create your models here.
class Alumno(models.Model):
    matricula = models.CharField(max_length=11)
    