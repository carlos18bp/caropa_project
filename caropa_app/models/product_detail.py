from django.db import models

class ProductDetail(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.name
