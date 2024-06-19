import re
from django.core.exceptions import ValidationError
from django.db import models
from django_attachments.fields import GalleryField
from django_attachments.models import Library
from caropa_app.models import Category, Color, HomeCategory, ProductDetail, Size

def validate_ref(value):
    """
    Validator for product reference. Ensures the reference contains only uppercase letters and numbers without spaces.

    Args:
        value (str): The reference value to validate.

    Raises:
        ValidationError: If the reference contains characters other than uppercase letters and numbers.
    """
    if not re.match(r'^[A-Z0-9]+$', value):
        raise ValidationError('Reference must contain only uppercase letters and numbers, and no spaces.')

class Product(models.Model):
    """
    Product model to define product details, categories, and other attributes.

    Attributes:
        ref (str): Reference code for the product.
        categories (ManyToManyField): Categories associated with the product.
        home_categories (ManyToManyField): Home categories associated with the product.
        trending_now (bool): Indicates if the product is trending. Default is False.
        product_detail (ForeignKey): Foreign key to the ProductDetail model.
        size (ForeignKey): Foreign key to the Size model.
        color (ForeignKey): Foreign key to the Color model.
        stock (int): Stock quantity of the product.
        gallery (GalleryField): Gallery field for attaching images to the product.
    """
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
        """
        String representation of the Product object.

        Returns:
            str: The reference code, product name, and stock quantity.
        """
        return f'{self.ref} ({self.product_detail.name_en} - Stock: {self.stock})'

    def delete(self, *args, **kwargs):
        """
        Custom delete method to ensure associated galleries are deleted.
        """
        try:
            if self.gallery:
                self.gallery.delete()
        except Library.DoesNotExist:
            pass
        super(Product, self).delete(*args, **kwargs)
