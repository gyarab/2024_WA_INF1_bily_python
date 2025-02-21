from django.shortcuts import render
from django.urls import reverse
from .models import Ciudad
import json

def ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'content/ciudades.html', {'ciudades': ciudades})

def ciudad(request, id):
    ciudad = Ciudad.objects.get(id=id)
    return render(request, 'content/ciudad.html', {'ciudad': ciudad})

def galeria(request):
    imagenes = [
    ]
    return render(request, "content/galeria.html", {"imagenes": imagenes})

def provincias(request):
    return render(request, "content/provincias.html")

def provincia(request, id):
    return render(request, "content/provincia.html")

def categorias(request):
    return render(request, "content/categorias.html")

def categoria(request, id):
    return render(request, "content/categoria.html")