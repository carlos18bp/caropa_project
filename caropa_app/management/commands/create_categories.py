from caropa_app.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create predefined categories'

    def handle(self, *args, **options):
        categories = [
            {"name": "Handmade", "is_primary": True},
            {"name": "Skirts", "is_primary": True},
            {"name": "Denim", "is_primary": True},
            {"name": "Blouses", "is_primary": True},
            {"name": "Dresses", "is_primary": True},
            {"name": "Trousers", "is_primary": True},
            {"name": "Swimwear", "is_primary": True},
            {"name": "Sets", "is_primary": True},
            {"name": "Accessories", "is_primary": True},
            {"name": "Sale", "is_primary": True},
            {"name": "Category (checked)", "is_primary": False},
            {"name": "Category (checked hover)", "is_primary": False},
            {"name": "Category (unchecked)", "is_primary": False},
            {"name": "Category (unchecked hover)", "is_primary": False},
            {"name": "Category (unchecked)", "is_primary": False}
        ]

        for category_data in categories:
            Category.objects.get_or_create(name=category_data["name"], defaults={"is_primary": category_data["is_primary"]})
        
        self.stdout.write(self.style.SUCCESS('Predefined categories created successfully'))
