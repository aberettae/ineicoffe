from django.conf.urls import url
from .views import ReservaView, DetalleReservaView
urlpatterns = [
    url(r'^nueva/$', ReservaView.as_view(), name='nueva'),
    url(r'^detalle/(?P<pk>[0-9a-zA-Z]+)/$', DetalleReservaView.as_view(), name='detalle')
]