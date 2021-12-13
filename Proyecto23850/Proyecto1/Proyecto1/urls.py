"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path



#Importar las vistas --> Primer Metodo
from Proyecto1.views import saludo
from Proyecto1.views import segundaVista
from Proyecto1.views import diaDeHoy
from Proyecto1.views import apellido
from Proyecto1.views import probandoTemplate





#Importar las vista --> Segundo Metodo
#from Proyecto1.views import saludo, segundaVista, diaDeHoy




urlpatterns = [
    path('admin/', admin.site.urls),

    #Generar la nueva URL "direccion en la web/" ---> la otra es de la views.py
 
    path("saludo/", saludo),

    path("index2/", segundaVista),

    path("dia/", diaDeHoy),

    path("apellido/<ape>", apellido), #se crea un input

    path("probandoTemplate/", probandoTemplate),
    
]
