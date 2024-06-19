from django.core.exceptions import ValidationError
from django.db import models
from caropa_app.models import Product

class SoldProduct(models.Model):
    """
    Model representing a sold product.
    
    Attributes:
        product (ForeignKey): Reference to the Product model.
        color_selected (str): Color selected for the sold product.
        quantity (int): Quantity of the product sold.
    """
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    color_selected = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        """
        String representation of the SoldProduct object.

        Returns:
            str: The name of the product, selected color, and quantity sold.
        """
        return f'{self.product.product_detail.name} ({self.color_selected} - Qty: {self.quantity})'
    
    def save(self, *args, **kwargs):
        """
        Custom save method to update stock quantity when a SoldProduct is created.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        
        Raises:
            ValidationError: If there is not enough stock available.
        """
        if self.pk is None:  # Only decrease stock when creating a new SoldProduct
            self.product.stock -= self.quantity
            if self.product.stock < 0:
                raise ValidationError('Not enough stock available.')
            self.product.save()
        super(SoldProduct, self).save(*args, **kwargs)

class Sale(models.Model):
    """
    Model representing a sale.
    
    Attributes:
        email (str): Email of the customer.
        address (str): Address of the customer.
        city (str): City of the customer.
        state (str): State of the customer.
        postal_code (str): Postal code of the customer.
        sold_products (ManyToManyField): Sold products associated with the sale.
        tracking_number (str): Tracking number for the sale, optional.
    """
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    sold_products = models.ManyToManyField(SoldProduct)
    tracking_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """
        String representation of the Sale object.

        Returns:
            str: The email of the customer.
        """
        return self.email
    
    def delete(self, *args, **kwargs):
        """
        Custom delete method to delete all sold products associated with the sale.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # Delete all sold products associated with this sale
        for sold_product in self.sold_products.all():
            sold_product.delete()
        # Call the superclass delete method
        super().delete(*args, **kwargs)
