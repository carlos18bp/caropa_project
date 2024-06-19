from django.db import models

class Size(models.Model):
    """
    Size model to define different sizes.

    Attributes:
        name (str): Name of the size with a maximum length of 50 characters.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        """
        String representation of the Size object.

        Returns:
            str: The name of the size.
        """
        return self.name
