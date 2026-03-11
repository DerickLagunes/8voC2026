from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core import views as core
from estudiantes_api import views as estudiantes

urlpatterns = [
    #Paths con 3 parametros: endpoint, controller, nombre
    path('', core.index, name='index'),
    path('derick/', core.derick, name='derick'),
    path('estudiantes/', include('estudiantes_api.urls')),
    path('usuarios/', include('usuarios.urls')),
    
    # Endpoint para iniciar sesión (recibe email y password, devuelve access y refresh tokens)
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Endpoint para refrescar el token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
