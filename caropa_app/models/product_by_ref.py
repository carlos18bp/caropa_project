import re
from django.db import models
from django.core.exceptions import ValidationError

def validate_ref(value):
    if not re.match(r'^[A-Z0-9]+$', value):
        raise ValidationError('Reference must contain only uppercase letters and numbers, and no spaces.')

class ProductByRef(models.Model):
    ref = models.CharField(max_length=20, validators=[validate_ref])

    def __str__(self):
        return self.ref