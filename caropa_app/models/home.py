import re
from django.core.exceptions import ValidationError
from django.db import models
from django_attachments.fields import GalleryField
from django_attachments.models import Library

def validate_title(value):
    """
    Validator for title fields. Ensures the title contains only uppercase letters, numbers, and spaces.

    Args:
        value (str): The title value to validate.

    Raises:
        ValidationError: If the title contains characters other than uppercase letters, numbers, and spaces.
    """
    if not re.match(r'^[A-Z0-9 ]+$', value):
        raise ValidationError('Title must contain only uppercase letters, numbers, and spaces.')

class Banner(models.Model):
    """
    Banner model to define banner text in different languages.

    Attributes:
        text_en (str): Text of the banner in English.
        text_es (str): Text of the banner in Spanish for language toggle purposes.
    """
    text_en = models.CharField(max_length=200)

    # Field for language toggle purpose.
    text_es = models.CharField(max_length=200)

    def __str__(self):
        """
        String representation of the Banner object.

        Returns:
            str: The text of the banner in English.
        """
        return self.text_en

class HomeCategory(models.Model):
    """
    HomeCategory model to define categories displayed on the home page.

    Attributes:
        title_en (str): Title of the category in English.
        image (ImageField): Image associated with the category.
        title_es (str): Title of the category in Spanish for language toggle purposes.
    """
    title_en = models.CharField(max_length=100, validators=[validate_title])
    image = models.ImageField(upload_to='home/categories/')

    # Field for language toggle purpose.
    title_es = models.CharField(max_length=100, validators=[validate_title])

    def __str__(self):
        """
        String representation of the HomeCategory object.

        Returns:
            str: The title of the category in English.
        """
        return self.title_en
    
    class Meta:
        verbose_name = "Home Category"
        verbose_name_plural = "Home Categories"

class Home(models.Model):
    """
    Home model to define the structure and content of the home page.

    Attributes:
        carousel_presentation (GalleryField): Gallery for the carousel presentation.
        section_3_title_en (str): Title for section 3 in English.
        section_3_description_en (str): Description for section 3 in English.
        section_3_gallery (GalleryField): Gallery for section 3.
        section_5_title_en (str): Title for section 5 in English.
        section_5_description_en (str): Description for section 5 in English.
        section_5_image (ImageField): Image for section 5.
        section_3_title_es (str): Title for section 3 in Spanish.
        section_3_description_es (str): Description for section 3 in Spanish.
        section_5_title_es (str): Title for section 5 in Spanish.
        section_5_description_es (str): Description for section 5 in Spanish.
    """
    carousel_presentation = GalleryField(related_name='homes_with_carousel', on_delete=models.CASCADE)
    section_3_title_en = models.CharField(max_length=100)
    section_3_description_en = models.TextField()
    section_3_gallery = GalleryField(related_name='homes_with_section_3_gallery', on_delete=models.CASCADE)
    section_5_title_en = models.CharField(max_length=100)
    section_5_description_en = models.TextField()
    section_5_image = models.ImageField(upload_to='home/images/')

    # Field for language toggle purpose.
    section_3_title_es = models.CharField(max_length=100)
    section_3_description_es = models.TextField()
    section_5_title_es = models.CharField(max_length=100)
    section_5_description_es = models.TextField()

    def __str__(self):
        """
        String representation of the Home object.

        Returns:
            str: The identifier of the home instance.
        """
        return f'Home {self.id}'

    def delete(self, *args, **kwargs):
        """
        Custom delete method to ensure associated galleries are deleted.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        try:
            if self.carousel_presentation:
                self.carousel_presentation.delete()
            if self.section_3_gallery:
                self.section_3_gallery.delete()
        except Library.DoesNotExist:
            pass
        super(Home, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"
