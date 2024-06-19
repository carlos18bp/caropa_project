from rest_framework import serializers
from caropa_app.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.

    This serializer converts Category model instances to JSON format and vice versa.
    """
    class Meta:
        model = Category
        fields = '__all__'
