from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo, segunda_vista, dia_de_hoy, mi_nombre, template1, template2, template3, template4, template5

urlpatterns = [
    path('saludo/', saludo),
    path('segundavista/', segunda_vista),
    path('diadehoy/', dia_de_hoy),
    path('prueba4/<nombre>', mi_nombre),
    path('template1/', template1),
    path('template2/', template2),
    path('template3/', template3),
    path('template4/<nombre>', template4),
    path('template5/', template5),
    path('admin/', admin.site.urls),
]
