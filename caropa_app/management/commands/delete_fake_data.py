from caropa_app.models import Product, Category, Home, Banner, HomeCategory
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create rake records in the database'

    """
    To delete fake data via console, run:
    python3 manage.py delete_fake_data
    """
    def handle(self, *args, **options):
        Banner.objects.all().delete()
        Category.objects.all().delete()
        HomeCategory.objects.all().delete()
        for product in Product.objects.all():
            product.delete()

        for home in Home.objects.all():
            home.delete()