import re
from django.db import models
from django.core.exceptions import ValidationError
from django_attachments.fields import GalleryField
from django_attachments.models import Library
from .product import Product 

def validate_title(value):
    if not re.match(r'^[A-Z0-9 ]+$', value):
        raise ValidationError('Title must contain only uppercase letters, numbers, and spaces.')

class Banner(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class HomeCategories(models.Model):
    title = models.CharField(max_length=100, validators=[validate_title])
    image = models.ImageField(upload_to='Home/categories/')
    products = models.ManyToManyField(Product, related_name='home_categories')

    def __str__(self):
        return self.title

    def clean(self):
        if HomeCategories.objects.count() >= 12:
            raise ValidationError("You can only create a maximum of 12 HomeCategories.")

    class Meta:
        verbose_name = "Home Category"
        verbose_name_plural = "Home Categories"


class Home(models.Model):
    banners = models.ManyToManyField(Banner, related_name='home_banners')
    carousel_presentation = GalleryField(related_name='homes_with_carousel', on_delete=models.CASCADE)
    section_3_title = models.CharField(max_length=100, validators=[validate_title])
    section_3_description = models.TextField()
    section_3_gallery = GalleryField(related_name='homes_with_section_3_gallery', on_delete=models.CASCADE)

    def __str__(self):
        return f'Home {self.id}'

    def delete(self, *args, **kwargs):
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
        verbose_name_plural = "Homes"
