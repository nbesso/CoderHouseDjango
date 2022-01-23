from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo, segunda_vista, dia_de_hoy, mi_nombre

urlpatterns = [
    path('saludo/', saludo),
    path('segundavista/', segunda_vista),
    path('diadehoy/', dia_de_hoy),
    path('prueba4/<nombre>', mi_nombre),
    path('admin/', admin.site.urls),
]
