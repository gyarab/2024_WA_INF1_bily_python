from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ciudad, ciudades, galeria, provincia, provincias, categoria, categorias, register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

app_name = 'content'

urlpatterns = [
    path('ciudades/', ciudades, name='ciudades'),
    path('ciudades/<int:id>/', ciudad, name='ciudad'),
    path('galeria/', galeria, name='galeria'),
    path('provincias/', provincias, name='provincias'),
    path('provincias/<int:id>/', provincia, name='provincia'),
    path('categorias/', categorias, name='categorias'),
    path('categorias/<int:id>/', categoria, name='categoria'),
    path('', ciudades, name='index'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register/', register, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)