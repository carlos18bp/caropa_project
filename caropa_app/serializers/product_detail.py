from caropa_app.models import ProductDetail
from rest_framework import serializers

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'
