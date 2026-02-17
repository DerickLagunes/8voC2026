from django.contrib import admin
from django.urls import path

from core import views as core
from alumno import views as alumno
from registro import views as registro
from error_reports import views as error_reports

urlpatterns = [
    #Paths con 3 parametros: endpoint, controller, nombre
    path('', core.index, name='index'),
    path('derick/', core.derick, name='derick'),
    path('daniel/', core.daniel, name='daniel'),
    path('alumno/', alumno.contacto_view, name='alumno'),
    path('registro/', registro.registro_view, name='registro'),
    path('reportes-error/', error_reports.reporte_error, name='reporte_error'),
    path('obtener-reportes/', error_reports.obtener_reportes, name='obtener_reportes'),
]
