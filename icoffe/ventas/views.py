from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from productos.models import Producto

def demo_vista_basica(request):
    return HttpResponse('Hola mundo, esta es una vista basica')

def carta_productos(request):
    template = 'carta_productos.html'
    context = {
        "titulo": "Carta de productos",
        "productos": Producto.objects.all()
    }
    return render(request, template, context)