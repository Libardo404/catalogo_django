# app_catalogo/views.py
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from .datos import LIBROS, buscar_libro

def inicio(request):
    contexto = {"nombre_sitio": "Catálogo ADSO", "total": len(LIBROS)}
    return render(request, "catalogo/inicio.html", contexto)

def lista_libros(request):
    genero = request.GET.get("genero", "") # "" si no viene ?genero= en la dirección
    if genero:
        libros = [libro for libro in LIBROS if libro["genero"] == genero]
    else:
        libros = LIBROS
    return render(request, "catalogo/lista.html", {"libros": libros, "genero":
genero})

def detalle_libro(request, libro_id):
    libro = buscar_libro(libro_id)
    if libro is None:
        raise Http404("El libro no existe")
    return render(request, "catalogo/detalle.html", {"libro": libro})

class AcercaView(TemplateView):
    template_name = "catalogo/acerca.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["version"] = "1.0"
        return contexto