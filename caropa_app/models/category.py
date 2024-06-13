from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_primary = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
