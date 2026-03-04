from django.contrib import admin
from django.urls import path, include

from core import views as core
from estudiantes_api import views as estudiantes

urlpatterns = [
    #Paths con 3 parametros: endpoint, controller, nombre
    path('', core.index, name='index'),
    path('derick/', core.derick, name='derick'),
    path('estudiantes/', include('estudiantes_api.urls')),
]
