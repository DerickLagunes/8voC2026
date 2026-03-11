from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegistroSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistroView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistroSerializer
