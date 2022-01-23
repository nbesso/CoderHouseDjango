from django.http import HttpResponse
from datetime import datetime


def saludo(request):
    return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<h1>Hola!</h1></br><p>Recuerden que esa es mi segunda vista</p>")


def dia_de_hoy(request):
    hoy = datetime.now()
    message = f"<h1>Hola!</h1></br><p>Recuerden que hoy es {hoy}</p>"
    return HttpResponse(message)


def mi_nombre(request, nombre):
    message = f"<h1>Hola!</h1></br><p>Recuerden que la persona conctada es {nombre}</p>"
    return HttpResponse(message)