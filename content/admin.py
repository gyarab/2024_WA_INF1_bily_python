from django.contrib import admin
from .models import Resena, Ciudad, Categoria, Provincia, Imagen

class ImagenEnlinea(admin.TabularInline):
    model = Imagen
    extra = 1

class CiudadAdmin(admin.ModelAdmin):
    inlines = [ImagenEnlinea]

admin.site.register(Categoria)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Provincia)
admin.site.register(Resena)
