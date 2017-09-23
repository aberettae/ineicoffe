from django.db import models
from ambientes.models import Mesa
from productos.models import Producto
from recursoshumanos.models import Personal


# Create your models here.
class Pedido(models.Model):
    #id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    nota = models.TextField(blank=True, null=True, default=None)
    mesa = models.ManyToManyField(Mesa)
    nro_clientes = models.PositiveIntegerField()
    personal = models.ForeignKey(Personal)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)


class DetallePedido(models.Model):
    producto = models.ForeignKey(Producto)
    pedido = models.ForeignKey(Pedido)
    precio = models.DecimalField(max_digits=7, decimal_places=3)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
