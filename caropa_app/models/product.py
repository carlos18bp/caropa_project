import re
from django.db import models
from django_attachments.fields import GalleryField
from django.core.exceptions import ValidationError
from caropa_app.models import ProductDetail, Category, Size, Color, ProductByRef

def validate_ref(value):
    if not re.match(r'^[A-Z0-9]+$', value):
        raise ValidationError('Reference must contain only uppercase letters and numbers, and no spaces.')

class Product(models.Model):
    ref = models.ForeignKey(ProductByRef, related_name='products', on_delete=models.PROTECT)
    product_detail = models.ForeignKey(ProductDetail, related_name='products', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='products')
    size = models.ForeignKey(Size, related_name='products', on_delete=models.PROTECT)
    color = models.ForeignKey(Color, related_name='products', on_delete=models.PROTECT)
    
    gallery = GalleryField(related_name='products_with_attachment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ref} ({self.product_detail.name})'

    def delete(self, *args, **kwargs):
        if self.product_detail:
            self.product_detail.delete()
        if self.gallery:
            self.gallery.delete()
        super(Product, self).delete(*args, **kwargs)