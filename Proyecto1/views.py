from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
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


def template1(request):
    return render(request, "template1.html")

def template2(request):
    return render(request, "template2.html")

def template3(request):
    curso = "Python"
    context = {"curso": "python"}
    return render(request, "template3.html", context)

def template4(request, nombre):
    context = {"nombre": nombre}
    return render(request, "template4.html", context)

def template5(request):
    context = {"lista": [1,2,3,4]}
    return render(request, "template5.html", context)

