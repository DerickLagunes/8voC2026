import base64
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField()
    carrera = models.CharField(max_length=100)
    promedio = models.FloatField()

    # CAMPO PARA GUARDAR LA IMAGEN EN EL BACK (carpeta media)
    foto = models.ImageField(upload_to='estudiantes/', blank=True, null=True)

    # CAMPO BINARIO PARA LA IMAGEN EN LA BD
    foto_binaria = models.BinaryField(blank=True, null=True)

    def estudiar(self):
        pass

    def inscribirse(self):
        pass

    def __str__(self):
        return self.nombre
        
    @property
    def foto_base64(self):
        if self.foto_binaria:
            # Convierte los bytes a un string codificado en base64
            codificado = base64.b64encode(self.foto_binaria).decode('utf-8')
            return f"data:image/jpeg;base64,{codificado}"
        return None
