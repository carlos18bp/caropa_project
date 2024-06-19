from rest_framework import serializers
from caropa_app.models import Product
from caropa_app.serializers import (
    CategorySerializer,
    ColorSerializer,
    ProductDetailSerializer,
    SizeSerializer,
)

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    This serializer converts Product model instances to JSON format and vice versa.
    It also includes nested serializers for related models.
    """
    product_detail = ProductDetailSerializer()
    categories = CategorySerializer(many=True)
    size = SizeSerializer()
    color = ColorSerializer()
    gallery_urls = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_gallery_urls(self, obj):
        """
        Retrieves the URLs of all images in the gallery associated with the Product instance.
        
        Args:
            obj (Product): The Product instance.
        
        Returns:
            list: A list of absolute URLs of the images in the gallery.
        """
        request = self.context.get('request')
        if obj.gallery:
            return [request.build_absolute_uri(attachment.file.url) for attachment in obj.gallery.attachment_set.all()]
        return []
