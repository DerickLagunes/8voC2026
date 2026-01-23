from django.shortcuts import render

def index(request):
    return render(request, 'core/lore.html')  # ← Nota el 'core/' agregado

#def carreras(request):
   # return render(request, 'core/carreras.html')
  # def index(request):
   # return render(request, 'core/index.html') 