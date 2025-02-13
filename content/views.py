from django.shortcuts import render
from django.urls import reverse
from .models import Ciudad
import json

def ciudades(request):
    articles = Ciudad.objects.all()
    return render(request, 'content/ciudades.html', {'ciudades': ciudades})

def ciudad(request, id):
    article = Ciudad.objects.get(id=id)
    return render(request, 'content/ciudad.html', {'ciudad': ciudad})

def galeria(request):
    images = [
        {"url": "/media/gallery/image1.jpg", "caption": "Image 1"},
        {"url": "/media/gallery/image2.jpg", "caption": "Image 2"},
        {"url": "/media/gallery/image3.jpg", "caption": "Image 3"},
    ]
    return render(request, "content/gallery.html", {"images": images})

def provincias(request):
    return render(request, "content/authors.html")

def provincia(request, id):
    return render(request, "content/author.html")

def categorias(request):
    return render(request, "content/categories.html")

def categoria(request, id):
    return render(request, "content/category.html")