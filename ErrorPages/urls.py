from django.contrib import admin
from django.urls import path

from core import views as core
from alumno import views as alumno
from contacto_mysql import views as contacto

urlpatterns = [
    #Paths con 3 parametros: endpoint, controller, nombre
    path('', core.index, name='index'),
    path('derick/', core.derick, name='derick'),
    path('karol/', core.karol, name='karol'),
    path('alumno/',alumno.contacto_view,name='alumno'),
]
