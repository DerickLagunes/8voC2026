# views.py #

from django.shortcuts import render
from alumno.alumno import alumno

from django.shortcuts import render
from .forms import ContactoForm

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Los datos ya pasaron las validaciones de front y back
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            
            print(f"--- NUEVO MENSAJE ---")
            print(f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}")
            
            return render(request, 'alumno/informacion.html', {'form': form, 'success': True})
    else:
        form = ContactoForm()
    
    return render(request, 'alumno/informacion.html', {'form': form})