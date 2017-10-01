from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView
from .models import Pedido, DetallePedido
from apps.productos.models import Producto, Categoria
from .forms import PedidoForm

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


class CrearOrdenView(FormView):
    form_class = PedidoForm
    template_name = 'ventas/crear_orden.html'
    success_url = reverse_lazy('ventas:lista-pedidos')
    
    def get_context_data(self, **kwargs):
        context = super(CrearOrdenView, self).get_context_data(**kwargs)
        context.update({
            "categorias": Categoria.objects.all(),
            "productos": Producto.objects.filter(stock__gt=0).order_by('-precio', 'nombre')
        })

        return context


class ListaPedidoView(ListView):
    template_name = 'ventas/lista_pedidos.html'
    model = Pedido
