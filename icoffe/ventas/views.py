from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

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


class CartaProductos(TemplateView):
    template_name = 'carta_productos.html'
    
    def get_context_data(self, **kwargs):
        contex = super(CartaProductos, self).get_context_data(**kwargs)
        contex.update({
            "titulo": "Carta de productos",
            "productos": Producto.objects.all()
        })

        return contex


class ProductoLista(ListView):
    template_name = 'productos_lista.html'
    model = Producto
    context_object_name = 'productos'

    def get_queryset(self):
        categortia = self.kwargs.get('categoria')
        if categortia is None:
            return Producto.objects.all()
        else:
            return Producto.objects.filter(categoria_id=categortia)

    def get_context_data(self, **kwargs):
        context = super(ProductoLista, self).get_context_data(**kwargs)
        context.update({
            "titulo": "Carta de productos / listview"
        })

        return context
