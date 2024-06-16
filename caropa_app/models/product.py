import re
from django.db import models
from django_attachments.fields import GalleryField
from django.core.exceptions import ValidationError
from caropa_app.models import ProductDetail, Category, HomeCategory, Size, Color
from django_attachments.models import Library

def validate_ref(value):
    if not re.match(r'^[A-Z0-9]+$', value):
        raise ValidationError('Reference must contain only uppercase letters and numbers, and no spaces.')

class Product(models.Model):
    ref = models.CharField(max_length=20, validators=[validate_ref])    
    categories = models.ManyToManyField(Category, related_name='products')
    home_categories = models.ManyToManyField(HomeCategory, related_name='home_categories')
    trending_now = models.BooleanField(default=False)
    product_detail = models.ForeignKey(ProductDetail, related_name='products', on_delete=models.PROTECT)
    size = models.ForeignKey(Size, related_name='products', on_delete=models.PROTECT)
    color = models.ForeignKey(Color, related_name='products', on_delete=models.PROTECT)
    stock = models.IntegerField(default=1, null=False, blank=False)
    
    gallery = GalleryField(related_name='products_with_attachment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ref} ({self.product_detail.name} - Stock: {self.stock})'

    def delete(self, *args, **kwargs):
        try:
            if self.gallery:
                self.gallery.delete()
        except Library.DoesNotExist:
            pass
        super(Product, self).delete(*args, **kwargs)
