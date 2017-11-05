from django.conf.urls import url
from .views import ProductosApiView, CategoriaAPiView, CategoriaListApiView

urlpatterns = [
    url(r'^$', ProductosApiView.as_view(), name="lista"),
    url(r'^categoria/detalle/(?P<pk>[1-9]{1,3})/$', CategoriaAPiView.as_view(), name="categoria"),
    url(r'^categoria/lista/$', CategoriaListApiView.as_view(), name="categoria_lista"),
    url(r'^categoria/(?P<categoria>[1-9]{1,3})/$', ProductosApiView.as_view(), name="lista_categoria")
]
