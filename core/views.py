from django.shortcuts import render

# Create your views here.
def index(request):
    print("alguien entro a la página principal")
    return render(request, 'core/index.html')

def katia(request):
    return render(request, 'core/katia.html')