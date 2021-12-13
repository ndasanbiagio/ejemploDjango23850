from django.http import HttpResponse
from datetime import datetime

from django.template import Template, Context


def saludo(request):

    return HttpResponse("Hola Django")


def segundaVista(request):

    return HttpResponse("<br>---Ya somos programadores---")



def diaDeHoy(request):

    variable = datetime.now()

    return HttpResponse(f"Hoy es un gran día <br>{variable}")


def apellido(request, ape):

    fecha = datetime.now()
    return HttpResponse(f"El Profe es {ape}, explica bien .. <br> Por lo menos hoy {fecha}")


def probandoTemplate(request):

    miHTML = open("F:/CoderHouse/Python/Django/Prueba_3/plantillas/template1.html")

    plantilla = Template(miHTML.read())

    miHTML.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)