from django.conf.urls import url
from .views import (
    CartaProductos,
    ProductoLista,
    CrearOrdenView,
    ListaPedidoView
)

urlpatterns = [
    url(r'^carta/$', CartaProductos.as_view()),
    url(r'^lista-productos/(?P<categoria>[1-9]{1,3})?/?$', ProductoLista.as_view()),
    url(r'^crear-orden/$', CrearOrdenView.as_view(), name='crear-orden'),
    url(r'^pedidos/$', ListaPedidoView.as_view(), name='lista-pedidos'),
]