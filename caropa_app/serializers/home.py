from rest_framework import serializers
from caropa_app.models import Home, Banner, HomeCategories

class BannerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Banner model.
    Serializes the text field of the Banner model.
    """
    class Meta:
        model = Banner
        fields = ['id', 'text']

class HomeCategoriesSerializer(serializers.ModelSerializer):
    """
    Serializer for the HomeCategories model.
    Serializes the title, image, and products fields.
    The image field is configured to return the URL of the image.
    """
    image = serializers.ImageField(use_url=True)  # This ensures the image field returns a URL

    class Meta:
        model = HomeCategories
        fields = ['id', 'title', 'image', 'products']

class HomeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Home model.
    Serializes the banners, carousel_presentation, section_3_title, section_3_description, and section_3_gallery fields.
    """
    banners = BannerSerializer(many=True)
    carousel_presentation = serializers.SerializerMethodField()
    section_3_gallery = serializers.SerializerMethodField()

    class Meta:
        model = Home
        fields = ['id', 'banners', 'carousel_presentation', 'section_3_title', 'section_3_description', 'section_3_gallery']

    def get_carousel_presentation(self, obj):
        """
        Method to get the URLs of the images in the carousel_presentation field.
        """
        return [image.file.url for image in obj.carousel_presentation.all()]

    def get_section_3_gallery(self, obj):
        """
        Method to get the URLs of the images in the section_3_gallery field.
        """
        return [image.file.url for image in obj.section_3_gallery.all()]
