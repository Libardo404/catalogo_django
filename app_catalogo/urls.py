# app_catalogo/urls.py
from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("libros/", views.lista_libros, name="lista_libros"),
    path("libros/<int:libro_id>/", views.detalle_libro, name="detalle_libro"),
    path("acerca/", views.AcercaView.as_view(), name="acerca"),
]