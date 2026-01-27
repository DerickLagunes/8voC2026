from django.shortcuts import render
from registro.registro import registro
from .forms import DataForm

def registro_view(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            # Los datos ya pasaron las validaciones de front y back
            nombre = form.cleaned_data['nombre']
            matricula = form.cleaned_data['matricula']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            rfc = form.cleaned_data['rfc']
            contrasena = form.cleaned_data['contrasena']
            
            print(f"--- NUEVO REGISTRO ---")
            print(f"Nombre: {nombre}\nMatrícula: {matricula}\nEmail: {email}\nTeléfono: {telefono}\nRFC: {rfc}\nContraseña: {contrasena}")
            
            return render(request, 'registro/registro.html', {'form': form, 'success': True})
    else:
        form = DataForm()
    
    return render(request, 'registro/registro.html', {'form': form})

# Create your views here.
