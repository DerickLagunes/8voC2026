from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        # Definimos qué campos queremos mostrar en el formulario
        fields = ['nombre', 'especie', 'edad', 'descripcion']
        
        # Opcional: Añadimos etiquetas personalizadas para que se vean mejor
        labels = {
            'nombre': 'Nombre de la mascota',
            'especie': '¿Qué animal es?',
            'edad': 'Edad (en años)',
            'descripcion': 'Cuéntanos algo sobre ella',
        }
        
        # Opcional: Podemos añadir estilos (como clases de CSS para Bootstrap)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Firulais'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }