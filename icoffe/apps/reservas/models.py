from django.db import models
from apps.ambientes.models import Ambiente,Mesa

# Create your models here.


class Reserva(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    nro_personas = models.PositiveIntegerField(default=1,
                                               help_text='Debe incluir a la person')
    fecha = models.DateTimeField()
    detalle = models.TextField(blank=True, null=True, default=None)
    mesa = models.ForeignKey(Mesa)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def get_codigo_ramdon(self):
        return 'ewewe9'

    def __str__(self):
        return self.codigo