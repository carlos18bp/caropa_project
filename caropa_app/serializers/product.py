from caropa_app.models import Product
from caropa_app.serializers import ProductDetailSerializer, CategorySerializer, SizeSerializer, ColorSerializer
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
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
        
        :param obj: The Product instance.
        :return: A list of absolute URLs of the images in the gallery.
        """
        request = self.context.get('request')
        if obj.gallery:
            return [request.build_absolute_uri(attachment.file.url) for attachment in obj.gallery.attachment_set.all()]
        return []
