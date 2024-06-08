from rest_framework import serializers
from caropa_app.models import ProductDetail

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'
