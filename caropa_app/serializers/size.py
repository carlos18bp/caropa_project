from rest_framework import serializers
from caropa_app.models import Size

class SizeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Size model.

    This serializer converts Size model instances to JSON format and vice versa.
    """
    class Meta:
        model = Size
        fields = '__all__'
