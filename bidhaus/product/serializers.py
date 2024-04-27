from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source="pk")  # dangerous

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "in_stock"]
