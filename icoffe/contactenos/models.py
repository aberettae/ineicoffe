from django.db import models

# Create your models here.


class Contacto(models.Model):
    TIPO_LISTA = (
        (1, 'Agradecimiento'),
        (2, 'Sugerencia'),
        (3, 'Reclamo')
    )

    ESTADO_LISTA = (
        (1, 'Recibido'),
        (2, 'En proceso'),
        (3, 'Resuelto')
    )
    id = models.AutoField(primary_key=True)
    tipo = models.PositiveIntegerField(choices=TIPO_LISTA)
    estado = models.PositiveSmallIntegerField(choices=ESTADO_LISTA, default=1)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True, default=None)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True, default=None)
    asunto = models.CharField(max_length=100)
    contenido = models.TextField(blank=True, null=True, default=None)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)