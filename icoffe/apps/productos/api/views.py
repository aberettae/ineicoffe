from core.apimixins import CreaMultiMixin
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .serializers import ProductoSerializer, CategoriaSerializer
from ..models import Producto, Categoria


class ProductosApiView(CreateAPIView, ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    def get_queryset(self):
        categoria = self.kwargs.get('categoria')
        if categoria is None:
            return Producto.objects.all()
        else:
            return Producto.objects.filter(categoria_id=categoria)

    def perform_create(self, serializer):
        data = serializer.data
        print(serializer.data)
        producto = Producto()
        producto.nombre = data['nombre']
        #Logica personalizada
        if data['stock'] < 100:
            producto.precio = float(data['precio']) + 5
        else:
            producto.precio = data['precio']

        try:
            categoria = Categoria.objects.get(nombre=data['categoria'].get('nombre'))
        except:
            categoria = Categoria(nombre=data['categoria'].get('nombre'))

        producto.stock = data['stock']
        producto.categoria = categoria
        producto.save()


class CategoriaListApiView(CreaMultiMixin, CreateAPIView, ListAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class CategoriaAPiView(DestroyAPIView, UpdateAPIView, RetrieveAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()