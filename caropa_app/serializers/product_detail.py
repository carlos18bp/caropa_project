from rest_framework import serializers
from caropa_app.models import ProductDetail

class ProductDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductDetail model.

    This serializer converts ProductDetail model instances to JSON format and vice versa.
    """
    class Meta:
        model = ProductDetail
        fields = '__all__'
