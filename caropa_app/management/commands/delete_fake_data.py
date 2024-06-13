from caropa_app.models import Product
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create rake records in the database'

    """
    To delete fake data via console, run:
    python3 manage.py delete_fake_data
    """
    def handle(self, *args, **options):
        for product in Product.objects.all():
            product.delete()