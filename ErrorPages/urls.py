from django.contrib import admin
from django.urls import path

from core import views as core

urlpatterns = [
    #Paths con 3 parametros: endpoint, controller, nombre
    path('', core.index, name='index'),
    path('derick/', core.derick, name='derick'),
    path('sergio/', core.sergio, name='sergio'),

]
