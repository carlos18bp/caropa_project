from rest_framework import serializers
from caropa_app.models import ProductByRef

class ProductByRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductByRef
        fields = '__all__'
