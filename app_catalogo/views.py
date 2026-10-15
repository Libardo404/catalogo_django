# app_catalogo/views.py
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse #Ejercicio 1

from .datos import LIBROS, buscar_libro

def inicio(request):         #Ejercicio 4
    # 1. Inicializamos los contadores antes de armar el contexto
    disponibles = 0
    prestados = 0

    # 2. Contamos recorriendo la lista de LIBROS
    for libro in LIBROS:
        if libro.get("disponible") == True:
            disponibles += 1
        else:
            prestados += 1

    # 3. Agregamos las nuevas claves manteniendo los datos originales
    contexto = {"nombre_sitio": "Catálogo ADSO", "total": len(LIBROS), "disponibles": disponibles, "prestados": prestados}

    return render(request, "catalogo/inicio.html", contexto)


def lista_libros(request):
    genero = request.GET.get("genero", "") # "" si no viene ?genero= en la dirección
    if genero:
        libros = [libro for libro in LIBROS if libro["genero"] == genero]
    else:
        libros = LIBROS
    return render(request, "catalogo/lista.html", {"libros": libros, "genero":
genero})


def detalle_libro(request, libro_id):        #todo: Ejercicio individual
    libro = buscar_libro(libro_id)
    if libro is None:
        raise Http404("El libro no existe")

    # Encontrar la posición del libro actual en la lista
    posicion = None
    for i, l in enumerate(LIBROS):
        if l["id"] == libro_id:
            posicion = i
            break

    # Calcular vecinos
    anterior = None
    siguiente = None

    if posicion is not None:
        if posicion > 0:
            anterior = LIBROS[posicion - 1]
        if posicion < len(LIBROS) - 1:
            siguiente = LIBROS[posicion + 1]

    contexto = {
        "libro": libro,
        "anterior": anterior,
        "siguiente": siguiente,
    }
    return render(request, "catalogo/detalle.html", contexto)


class AcercaView(TemplateView):
    template_name = "catalogo/acerca.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["version"] = "1.0"
        return contexto

def hola(request):                       #Ejercicio 1
    return HttpResponse("¡Hola, mundo!")

def cuadrado(request, numero):           #Ejercicio 2
    resultado = numero ** 2
    return HttpResponse(f"El cuadrado de {numero} es {resultado}.")

class ContactoView(TemplateView):        #Ejercicio 3
    template_name = "catalogo/contacto.html"

def autores(request):                    #Ejercicio 5
    # 1. Extraer autores únicos y ordenarlos alfabéticamente
    autores_unicos = sorted(list(set(libro["autor"] for libro in LIBROS if "autor" in libro)))
    
    # 2. Construir la lista de diccionarios con los conteos
    autores_calculados = []
    for nombre_autor in autores_unicos:
        # Contamos cuántas veces aparece este autor en la lista general
        cantidad_libros = sum(1 for libro in LIBROS if libro.get("autor") == nombre_autor)
        
        # Guardamos la estructura que nos pide el ejercicio
        autores_calculados.append({
            "autor": nombre_autor,
            "cantidad": cantidad_libros
        })
    
    # 3. Empacamos el resultado en el contexto
    contexto = {
        "autores": autores_calculados
    }
    
    # 4. Renderizamos la nueva plantilla
    return render(request, "catalogo/autores.html", contexto)

def sugerir(request):                    #Ejercicio 6
    # Inicializamos las variables que usará la plantilla
    titulo = ""
    error = ""
    enviado = False

    # 1. Comprobamos si el usuario envió el formulario usando el método POST
    if request.method == "POST":
        enviado = True
        # Obtener el dato del input cuyo atributo name es "titulo"
        # .strip() elimina espacios en blanco innecesarios al inicio y final
        titulo = request.POST.get("titulo", "").strip()
        
        # 2. Validamos si está vacío
        if not titulo:
            error = "Escribe un título"

    # 3. Empacamos el estado en el contexto
    contexto = {
        "titulo": titulo,
        "error": error,
        "enviado": enviado
    }

    return render(request, "catalogo/sugerir.html", contexto)