from rest_framework import serializers
from ..models import Producto, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')


class ProductoSerializer(serializers.ModelSerializer):
    #categoria = serializers.SlugRelatedField(slug_field='nombre', read_only=True)
    categoria = CategoriaSerializer()
    #categoria = serializers.HyperlinkedRelatedField(read_only=True, view_name="api_producto:categoria")
    insumo = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'stock', 'categoria', 'insumo')
