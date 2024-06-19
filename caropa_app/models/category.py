from django.db import models

class Category(models.Model):
    """
    Category model to define categories for different purposes.

    Attributes:
        name_en (str): Name of the category in English.
        is_primary (bool): Indicates if the category is primary. Default is True.
        name_es (str): Name of the category in Spanish for language toggle purposes.
    """
    name_en = models.CharField(max_length=100)
    is_primary = models.BooleanField(default=True)

    # Field for language toggle purpose.
    name_es = models.CharField(max_length=100)

    def __str__(self):
        """
        String representation of the Category object.

        Returns:
            str: The name of the category in English.
        """
        return self.name_en

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

