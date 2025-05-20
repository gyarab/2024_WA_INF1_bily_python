from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Ciudad
from .models import Provincia
from .models import Categoria
from .forms import ResenaForm
from .models import Resena
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import authenticate
import json

def ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'content/ciudades.html', {'ciudades': ciudades})

def ciudad(request, id):
    ciudad = Ciudad.objects.get(id=id)

    if request.method == "POST":
        review_form = ResenaForm(request.POST)
        if review_form.is_valid():
            review = Resena()
            review.name = review_form.cleaned_data["name"]
            review.rating = review_form.cleaned_data["rating"]
            review.text = review_form.cleaned_data["text"]
            review.city = ciudad
            review.save()
            return HttpResponseRedirect(reverse("content:ciudad", args=[ciudad.id]))

    review_form=ResenaForm()
    
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
    categorias = Categoria.objects.all()
    return render(request, "content/categorias.html", {"categorias": categorias})

def categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    return render(request, "content/categoria.html", {"categoria": categoria})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta ha sido creada. Ahora puedes iniciar sesión.')
            return redirect('content:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})