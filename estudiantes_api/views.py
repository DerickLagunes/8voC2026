from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import Estudiante
from .serializers import EstudianteSerializer
from django.contrib.auth import get_user_model

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
