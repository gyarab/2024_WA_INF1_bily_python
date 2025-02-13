from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import cities, city, gallery, provinces, province, categories, category

app_name = 'content'

urlpatterns = [
    path('cities/', cities, name='cities'),
    path('city/<int:id>/', city, name='city'),
    path('provinces/', provinces, name='provinces'),
    path('province/<int:id>/', province, name='province'),
    path('categories/', categories, name='categories'),
    path('category/<int:id>/', category, name='category'),
    path('gallery/', gallery, name='gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)