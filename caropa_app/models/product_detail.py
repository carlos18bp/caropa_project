from django.db import models

class ProductDetail(models.Model):
    """
    ProductDetail model to define the details of a product in different languages.

    Attributes:
        name_en (str): Name of the product in English.
        description_en (str): Description of the product in English.
        price (Decimal): Price of the product with a maximum of 100 digits and 2 decimal places.
        name_es (str): Name of the product in Spanish for language toggle purposes.
        description_es (str): Description of the product in Spanish for language toggle purposes.
    """
    name_en = models.CharField(max_length=200)
    description_en = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)

    # Fields for language toggle purpose.
    name_es = models.CharField(max_length=200)
    description_es = models.TextField()

    def __str__(self):
        """
        String representation of the ProductDetail object.

        Returns:
            str: The name of the product in English.
        """
        return self.name_en

