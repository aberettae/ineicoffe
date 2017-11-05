from rest_framework import serializers
from ..models import Producto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')


class ProductoSerializer(serializers.ModelSerializer):
    #categoria = serializers.SlugRelatedField(slug_field='nombre', read_only=True)
    categoria = CategoriaSerializer()
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'stock', 'categoria')
