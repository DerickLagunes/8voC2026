from django.contrib import admin
from django.urls import path, include

from core import views as core
<<<<<<< Updated upstream
=======
from alumno import views as alumno
from contacto_mysql import views as contacto
from estudiantes_api import views as estudiantes
>>>>>>> Stashed changes

urlpatterns = [
    #Paths con 3 parametros: endpoint, controller, nombre
    path('', core.index, name='index'),
    path('derick/', core.derick, name='derick'),
<<<<<<< Updated upstream
    path('gael/', core.gael, name='gael')
=======
    path('karol/', core.karol, name='karol'),
    path('alumno/',alumno.contacto_view,name='alumno'),
    path('estudiantes/', include('estudiantes_api.urls')),
>>>>>>> Stashed changes
]
