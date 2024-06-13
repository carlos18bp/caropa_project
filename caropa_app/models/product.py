import re
from django.db import models
from django_attachments.fields import GalleryField
from django.core.exceptions import ValidationError
from caropa_app.models import ProductDetail, Category, Size, Color
from django_attachments.models import Library
from django.apps import apps

def validate_ref(value):
    if not re.match(r'^[A-Z0-9]+$', value):
        raise ValidationError('Reference must contain only uppercase letters and numbers, and no spaces.')

class Product(models.Model):
    ref = models.CharField(max_length=20, validators=[validate_ref])    
    categories = models.ManyToManyField(Category, related_name='products')
    categories_home = models.ManyToManyField('caropa_app.HomeCategories', related_name='Home_Categories')
    trending_now = models.BooleanField(default=False)
    product_detail = models.ForeignKey(ProductDetail, related_name='products', on_delete=models.PROTECT)
    size = models.ForeignKey(Size, related_name='products', on_delete=models.PROTECT)
    color = models.ForeignKey(Color, related_name='products', on_delete=models.PROTECT)
    
    gallery = GalleryField(related_name='products_with_attachment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ref} ({self.product_detail.name})'

    def delete(self, *args, **kwargs):
        try:
            if self.gallery:
                self.gallery.delete()
        except Library.DoesNotExist:
            pass
        super(Product, self).delete(*args, **kwargs)

    @property
    def home_categories(self):
        HomeCategories = apps.get_model('caropa_app', 'HomeCategories')
        return HomeCategories.objects.filter(products=self)
