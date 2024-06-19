from django.db import models

class Color(models.Model):
    """
    Color model to define different colors.

    Attributes:
        name (str): Name of the color with a maximum length of 50 characters.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        """
        String representation of the Color object.

        Returns:
            str: The name of the color.
        """
        return self.name
