from django.db import models

# Create your models here.


class Ambiente(models.Model):
    TIPO_AMBIENTE = (
        (1, 'Interior'),
        (2, 'Exterior'),
        (3, 'Terraza'),
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True, default=None)
    tipo = models.PositiveIntegerField(choices=TIPO_AMBIENTE)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Mesa(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True)
    referencia = models.CharField(max_length=100, blank=True, null=True, default=None,
                                  help_text='referncia a la mesa')
    ambientes = models.ForeignKey(Ambiente)
    nro_asientos = models.PositiveIntegerField(default=4)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.codigo)
