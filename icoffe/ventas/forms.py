from django.forms import ModelForm
from .models import Pedido


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ('codigo', 'mesa', 'nota', 'nro_clientes', 'personal')

