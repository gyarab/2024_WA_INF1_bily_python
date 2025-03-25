from django import forms
from django.db import models
from django.utils.timezone import now  # Import timezone function

class Provincia(models.Model):
    name = models.CharField(max_length=200, default="Castilla la Mancha")

    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ciudad(models.Model):
    name = models.CharField(max_length=200, default="Nombre")
    perex = models.TextField(default="Perex")
    text = models.TextField(default="Texto")
    population = models.IntegerField(default=0)
    categories = models.ManyToManyField(Categoria, related_name='ciudades')
    province = models.ForeignKey(Provincia, on_delete=models.CASCADE, default="Castilla la Mancha")

    def __str__(self):
        return self.name
    
class Resena(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(default="Texto")
    rating = models.IntegerField(default=5)
    city = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review for {self.city.name} by {self.name}"
    
class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['name', 'text', 'rating']
        labels = {
            'name': 'Su nombre',
            'text': 'Texto',
            'rating': 'Estrellas'
        }
        help_texts = {
            'rating': "El valor debe estar entre 1 y 5"
        }
        error_messages = {
            'name': {
                'required': "Este campo es obligatorio"
            },
            "text": {
                "required": "Este campo es obligatorio"
            },
            "rating": {
                "required": "Este campo es obligatorio"
            }
        }

class Imagen(models.Model):
    city = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name="imagenes")
    image = models.ImageField(upload_to="ciudades/")
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.city.name}"