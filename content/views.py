from django.shortcuts import render
from django.urls import reverse
from .models import Ciudad
from .models import Provincia
from .models import Categoria
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
    provincias = Provincia.objects.all()
    return render(request, "content/provincias.html", {"provincias": provincias})

def provincia(request, id):
    provincia = Provincia.objects.get(id=id)
    return render(request, "content/provincia.html", {"provincia": provincia})

def categorias(request):
    categorias = Categoria.objects.all
    return render(request, "content/categorias.html", {"categorias": categorias})

def categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    return render(request, "content/categoria.html", {"categoria": categoria})