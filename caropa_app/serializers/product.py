from rest_framework import serializers
from caropa_app.models import Product
from caropa_app.serializers import ProductDetailSerializer, CategorySerializer, SizeSerializer, ColorSerializer

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

# Ejemplo de cómo usar el serializador:
# from rest_framework.renderers import JSONRenderer

# product_instance = Product.objects.first()
# serializer = ProductSerializer(product_instance, context={'request': request})
# json_data = JSONRenderer().render(serializer.data)
# print(json_data)
