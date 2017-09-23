from django.conf.urls import url
from .views import CartaProductos, ProductoLista
urlpatterns = [
    url(r'^carta/$', CartaProductos.as_view()),
    url(r'^lista-productos/(?P<categoria>[1-9]{1,3})?/?$', ProductoLista.as_view())
]