from django.db import models
from caropa_app.models import Product
from django.core.exceptions import ValidationError

class SoldProduct(models.Model):
    """
    Model representing a product in the cart.
    """
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    color_selected = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product.product_detail.name} ({self.color_selected} - Qty: {self.quantity})'
    
    def save(self, *args, **kwargs):
        if self.pk is None:  # Only decrease stock when creating a new SoldProduct
            self.product.stock -= self.quantity
            if self.product.stock < 0:
                raise ValidationError('Not enough stock available.')
            self.product.save()
        super(SoldProduct, self).save(*args, **kwargs)

class Sale(models.Model):
    """
    Model representing a sale.
    """
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    sold_products = models.ManyToManyField(SoldProduct)
    tracking_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.email
    
    def delete(self, *args, **kwargs):
        # Delete all sold products associated with this sale
        for sold_product in self.sold_products.all():
            sold_product.delete()
        # Call the superclass delete method
        super().delete(*args, **kwargs)
