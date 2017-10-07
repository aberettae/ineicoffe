"""icoffe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from apps.ventas.views import demo_vista_basica, carta_productos

urlpatterns = [
    url(r'^$', carta_productos, name='inicio'),
    url(r'^demo/$', demo_vista_basica),
    url(r'^ventas/', include('apps.ventas.urls', namespace='ventas')),
    url(r'^contactenos/', include('apps.contactenos.urls', namespace='contactenos')),
    url(r'^reserva/', include('apps.reservas.urls', namespace='reserva')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG is True:
    urlpatterns += [
        url(r'^demo/', include('apps.ejemplos.urls', namespace='ejemplos')),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)