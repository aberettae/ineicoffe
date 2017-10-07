from django.conf.urls import url
from .views import DemoView


urlpatterns = [
    url(r'^ejemplo/([1-9]{1,3})/(?P<reporte>[1-9]{1,3})/$', DemoView.as_view())
]