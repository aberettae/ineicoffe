from django.forms import ModelForm
from .models import Contacto


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ('tipo', 'primer_nombre', 'segundo_nombre', 'apellido_paterno',
                  'apellido_materno', 'asunto', 'contenido')
