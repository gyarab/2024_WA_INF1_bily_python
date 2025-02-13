from django.db import models
from django.utils.timezone import now  # Import timezone function

class Provincia(models.Model):
    name = models.CharField(max_length=200, default="Ciudad Real")

    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Ciudad(models.Model):
    name = models.CharField(max_length=200, default="Titulo")
    province = models.TextField(default="Perex")
    text = models.TextField(default="Text")
    population = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
    
class Resena(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    city = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Imagen(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="articles/")
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.article.title}"