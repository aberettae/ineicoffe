from django.conf.urls import url
from .views import ContactoView, AgradecimientoView

urlpatterns = [
    url(r'^buzon/$', ContactoView.as_view(), name='buzon'),
    url(r'^gracias/$', AgradecimientoView.as_view(), name='gracias')
]