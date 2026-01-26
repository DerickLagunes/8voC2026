# forms.py #

from django import forms
from django.core.exceptions import ValidationError
import re

class DataForm(forms.Form):

    nombre = forms.CharField(
        min_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre', 'pattern': '[a-zA-ZáéíóúÁÉÍÓÚ\\s]{10,}', 'title': 'Solo letras y espacios, mínimo 10 caracteres'})
    )
    matricula = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu matricula', 'pattern': '\\d{5}[A-Za-z]{2}\\d{3}', 'title': 'Formato: 5 dígitos, 2 letras, 3 dígitos (ej: 12345AB678)'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'})
    )
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu telefono', 'pattern': '\\d{10}', 'title': 'Exactamente 10 dígitos numéricos'})
    )
    rfc = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu RFC', 'pattern': '[A-Z]{4}\\d{6}[A-Z0-9]{3}', 'title': 'Formato: 4 letras mayúsculas, 6 números, 3 alfanuméricos (ej: ABCD123456XYZ)'})
    )
    contrasena = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Tu contraseña', 'pattern': '(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}', 'title': 'Mínimo 8 caracteres: mayúscula, minúscula, número y símbolo (@$!%*?&)', 'autocomplete': 'current-password'})
    )
    

    # Validación de Backend

    #Validación nombre
    #Solo letras y espacios. Sin números ni símbolos. Mínimo 10 caracteres.
    def clean_nombre(self):
        data = self.cleaned_data['nombre']
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]{10,}', data):
            raise ValidationError("El nombre solo puede contener letras y espacios.")
        if len(data) < 10:
            raise ValidationError("El nombre debe tener al menos 10 caracteres.")
        return data
    
    #Matrícula UTEZ (Texto)
    #Validación: Formato específico: 5 dígitos, 2 letras, 3 dígitos
    def clean_matricula(self):
        data = self.cleaned_data['matricula']
        if not re.match(r'^\d{5}[A-Za-z]{2}\d{3}$', data):
            raise ValidationError("La matrícula debe tener el formato: 5 dígitos, 2 letras, 3 dígitos.")
        return data

    #Correo Institucional (Email)
    #Validación: Debe ser un correo válido y forzosamente terminar en @utez.edu.mx
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@utez.edu.mx" not in data:
            raise ValidationError("Solo piuedes registrar correos de la utez")
        return data

    #Teléfono Móvil (Número)
    #Validación: Exactamente 10 dígitos numéricos. Sin espacios ni guiones
    def clean_telefono(self):
        data = self.cleaned_data['telefono']
        if not re.match(r'^\d{10}$', data):
            raise ValidationError("El teléfono debe contener exactamente 10 dígitos numéricos.")
        return data
    
    #RFC (Texto)
    #Validación: 4 letras, 6 números, 3 alfanuméricos. además: Mayúsculas obligatorias
    def clean_rfc(self):
        data = self.cleaned_data['rfc']
        if not re.match(r'^[A-Z]{4}\d{6}[A-Z0-9]{3}$', data):
            raise ValidationError("El RFC debe tener el formato: 4 letras mayúsculas, 6 números, 3 alfanuméricos.")
        return data

    #Contraseña (Password)
    #Validación: Mínimo 8 caracteres, al menos una mayúscula, una minúscula, un número y un símbolo especial (@$!%*?&).
    def clean_contrasena(self):
        data = self.cleaned_data['contrasena']
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', data):
            raise ValidationError("La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un símbolo especial (@$!%*?&).")
        return data