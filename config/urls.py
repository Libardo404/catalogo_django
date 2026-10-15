# config/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app_catalogo.urls")), # las rutas de la app quedan en la raíz del sitio
]