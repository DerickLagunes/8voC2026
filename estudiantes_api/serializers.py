from rest_framework import serializers
from .models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    # Campos virtuales, de apoyo
    foto_para_binario = serializers.ImageField(write_only=True, required=False)
    foto_base64_display = serializers.ReadOnlyField(source='foto_base64')

    class Meta:
        model = Estudiante
        fields = [
            'id', 'nombre', 'matricula', 'edad', 'carrera', 
            'promedio', 'foto', 'foto_para_binario', 'foto_base64_display'
        ]

    def create(self, validated_data):
        # Extraemos el segundo archivo (el que va a la base de datos), es nulo si no lo mandaron
        archivo_binario = validated_data.pop('foto_para_binario', None)

        # DRF guarda 'foto' automáticamente en la carpeta /media/
        estudiante = Estudiante.objects.create(**validated_data)

        # Si nos mandaron el segundo archivo, leemos sus bytes crudos y los guardamos
        if archivo_binario:
            # .read() extrae los bytes del archivo, ¡no se necesita base64 aquí!
            estudiante.foto_binaria = archivo_binario.read()
            estudiante.save()

        return estudiante
