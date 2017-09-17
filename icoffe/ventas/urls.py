from django.conf.urls import url
from .views import demovista, demo_orden, carta_productos

urlpatterns = [
    url(r'^$', demovista),
    url(r'^demo/$', demo_orden),
    url(r'^carta/$', carta_productos)
]