from rest_framework import serializers
from caropa_app.models import Color

class ColorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Color model.

    This serializer converts Color model instances to JSON format and vice versa.
    """
    class Meta:
        model = Color
        fields = '__all__'
