from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'contacto'