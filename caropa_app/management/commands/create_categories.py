from caropa_app.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create predefined categories'

    def handle(self, *args, **options):
        categories = [
            {"name_en": "Handmade (EN)", "name_es": "Handmade (ES)", "is_primary": True},
            {"name_en": "Skirts (EN)", "name_es": "Skirts (ES)", "is_primary": True},
            {"name_en": "Denim (EN)", "name_es": "Denim (ES)", "is_primary": True},
            {"name_en": "Blouses (EN)", "name_es": "Blouses (ES)", "is_primary": True},
            {"name_en": "Dresses (EN)", "name_es": "Dresses (ES)", "is_primary": True},
            {"name_en": "Trousers (EN)", "name_es": "Trousers (ES)", "is_primary": True},
            {"name_en": "Swimwear (EN)", "name_es": "Swimwear (ES)", "is_primary": True},
            {"name_en": "Sets (EN)", "name_es": "Sets (ES)", "is_primary": True},
            {"name_en": "Accessories (EN)", "name_es": "Accessories (ES)", "is_primary": True},
            {"name_en": "Sale (EN)", "name_es": "Sale (ES)", "is_primary": True},
            {"name_en": "Category (checked) (EN)", "name_es": "Category (checked) (ES)", "is_primary": False},
            {"name_en": "Category (checked hover) (EN)", "name_es": "Category (checked hover) (ES)", "is_primary": False},
            {"name_en": "Category (unchecked) (EN)", "name_es": "Category (unchecked) (ES)", "is_primary": False},
            {"name_en": "Category (unchecked hover) (EN)", "name_es": "Category (unchecked hover) (ES)", "is_primary": False},
            {"name_en": "Category (unchecked) (EN)", "name_es": "Category (unchecked) (ES)", "is_primary": False}
        ]

        for category_data in categories:
            Category.objects.get_or_create(
                name_en=category_data["name_en"],
                defaults={
                    "name_es": category_data["name_es"],
                    "is_primary": category_data["is_primary"]
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Predefined categories created successfully'))
