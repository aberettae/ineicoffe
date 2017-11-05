from django.conf.urls import url
from .views import ProductosApiView

urlpatterns = [
    url(r'^$', ProductosApiView.as_view(), name="lista"),
    url(r'^categoria/(?P<categoria>[1-9]{1,3})/$', ProductosApiView.as_view(), name="lista_categoria")
]
