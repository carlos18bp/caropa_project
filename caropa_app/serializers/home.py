from rest_framework import serializers
from caropa_app.models import Home, Banner, HomeCategories

class BannerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Banner model.
    Serializes the text field of the Banner model.
    """
    class Meta:
        model = Banner
        fields = "__all__"

class HomeCategoriesSerializer(serializers.ModelSerializer):
    """
    Serializer for the HomeCategories model.
    Serializes the title, image fields.
    The image field is configured to return the URL of the image.
    """
    image = serializers.ImageField(use_url=True)  # This ensures the image field returns a URL

    class Meta:
        model = HomeCategories
        fields = "__all__"

class HomeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Home model.
    Serializes the banners, carousel_presentation, section_3_title, section_3_description,
    section_3_gallery, section_5_title, section_5_description, and section_5_image fields.
    """
    carousel_presentation_urls = serializers.SerializerMethodField()
    section_3_gallery_urls = serializers.SerializerMethodField()
    section_5_image_url = serializers.ImageField(source='section_5_image', use_url=True)
    
    class Meta:
        model = Home
        fields = "__all__"

    def get_carousel_presentation_urls(self, obj):
        """
        Retrieves the URLs of all images in the carousel_presentation field.
        """
        request = self.context.get('request')
        if request and obj.carousel_presentation:
            return [request.build_absolute_uri(attachment.file.url) for attachment in obj.carousel_presentation.attachment_set.all()]
        return []

    def get_section_3_gallery_urls(self, obj):
        """
        Retrieves the URLs of all images in the section_3_gallery field.
        """
        request = self.context.get('request')
        if request and obj.section_3_gallery:
            return [request.build_absolute_uri(attachment.file.url) for attachment in obj.section_3_gallery.attachment_set.all()]
        return []
