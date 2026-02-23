from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Mascota

# 1. LISTAR (GET)
def api_lista_mascotas(request):
    mascotas = Mascota.objects.all().values()  # Convierte el QuerySet a diccionarios
    return JsonResponse(list(mascotas), safe=False)

# 2. CREAR (POST)
@csrf_exempt
def api_crear_mascota(request):
    if request.method == 'POST':
        # Intentamos leer datos de un formulario tradicional o un JSON
        nombre = request.POST.get('nombre')
        especie = request.POST.get('especie')
        edad = request.POST.get('edad')
        
        mascota = Mascota.objects.create(nombre=nombre, especie=especie, edad=edad)
        return JsonResponse({
            'mensaje': 'Mascota creada',
            'id': mascota.id
        }, status=201)

# 3. ACTUALIZAR (PUT/POST)
@csrf_exempt
def api_editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)

    if request.method == "PUT":
        data = json.loads(request.body)

        mascota.nombre = data.get("nombre", mascota.nombre)
        mascota.especie = data.get("especie", mascota.especie)
        mascota.edad = data.get("edad", mascota.edad)
        mascota.save()

        return JsonResponse({"mensaje": "Mascota actualizada"})

    return JsonResponse({"error": "Método no permitido"}, status=405)

# 4. ELIMINAR (DELETE)
@csrf_exempt
def api_eliminar_mascota(request, pk):
    if request.method == 'DELETE':
        mascota = get_object_or_404(Mascota, pk=pk)
        mascota.delete()
        return JsonResponse({'mensaje': 'Mascota eliminada'}, status=204)