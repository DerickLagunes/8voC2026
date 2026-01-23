
from django.contrib import admin
from django.urls import path
from core import views as core
urlpatterns = [
    #Phaths con 3 parametros : endpoint, controller, nombre
     #path('admin/', admin.site.urls),
    #path('', core.index, name='index'),
    path('', core.index, name='lore'),
    #path('carreras/', core.index, name='carreras'),
]
