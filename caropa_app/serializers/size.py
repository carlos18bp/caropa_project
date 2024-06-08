from rest_framework import serializers
from caropa_app.models import Size

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'
