# app_catalogo/urls.py
from django.urls import path
from . import views

app_name = "catalogo" # espacio de nombres: las rutas se llamarán "catalogo:..."

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("libros/", views.lista_libros, name="lista_libros"),
    path("libros/<int:libro_id>/", views.detalle_libro, name="detalle_libro"),
    path("acerca/", views.AcercaView.as_view(), name="acerca"),

    path("hola/", views.hola, name="hola"), #Ejercicio 1
    path("cuadrado/<int:numero>/", views.cuadrado, name="cuadrado"), #Ejercicio 2
    path("contacto/", views.ContactoView.as_view(), name="contacto"), #Ejercicio 3
    path("autores/", views.autores, name="autores"), #Ejercicio 5
    path("sugerir/", views.sugerir, name="sugerir"), #Ejercicio 6
]