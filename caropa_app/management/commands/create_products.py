import os
import random
from caropa_app.models import Category, Color, Product, ProductDetail, Size
from django.core.files import File
from django.core.management.base import BaseCommand
from django_attachments.models import Attachment, Library
from faker import Faker


class Command(BaseCommand):
    help = 'Create Product records in the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_products', type=int, nargs='?', default=10)

    def handle(self, *args, **options):
        number_of_products = options['number_of_products']
        fake = Faker()

        # List of test images
        test_images = [
            '/media/temp/product/product_temp1.webp',
            '/media/temp/product/product_temp2.webp',
            '/media/temp/product/product_temp3.webp',
            '/media/temp/product/product_temp4.webp',
        ]

        # List of predefined colors and sizes
        predefined_colors = ['red', 'blue', 'yellow', 'green', 'orange', 'violet', 'black', 'white', 'pink', 'rose']
        predefined_sizes = ['Small', 'Medium', 'Large', 'Extra Large']

        # Ensure the test images exist
        for image_path in test_images:
            if not os.path.isfile(os.getcwd() + image_path):
                self.stdout.write(self.style.ERROR(f'Image file {image_path} not found'))
                return

        primary_categories = list(Category.objects.filter(is_primary=True))
        non_primary_categories = list(Category.objects.filter(is_primary=False))

        for _ in range(number_of_products):
            ref_value = 'REF' + str(random.randint(1000, 9999))

            # Create a new ProductDetail
            product_detail = ProductDetail.objects.create(
                name=fake.word().capitalize(),
                description=fake.text(max_nb_chars=60),
                price=fake.random_int(min=1, max=100)
            )

            # Create a new gallery (library)
            gallery = Library.objects.create(title=fake.word())

            # Add test images to the gallery
            for image_path in test_images:
                image_path = os.getcwd() + image_path
                with open(image_path, 'rb') as image_file:
                    Attachment.objects.create(
                        library=gallery,
                        file=File(image_file, name=os.path.basename(image_path)),
                        original_name=os.path.basename(image_path),
                        rank=0  # You can set rank as needed
                    )

            used_combinations = set()

            for i in range(5):  # Create 5 products with the same reference

                # Select a unique predefined size and color combination
                while True:
                    size_name = random.choice(predefined_sizes)
                    color_name = random.choice(predefined_colors)
                    combination = (size_name, color_name)
                    if combination not in used_combinations:
                        used_combinations.add(combination)
                        break

                size, _ = Size.objects.get_or_create(name=size_name)
                color, _ = Color.objects.get_or_create(name=color_name)

                # Now create the product with the gallery
                new_product = Product.objects.create(
                    ref=ref_value,
                    product_detail=product_detail,
                    size=size,
                    color=color,
                    gallery=gallery  # Associate the gallery with the product
                )

                # Add a primary category and two non-primary categories to the product
                primary_category = random.choice(primary_categories)
                new_product.categories.add(primary_category)

                non_primary_category1, non_primary_category2 = random.sample(non_primary_categories, 2)
                new_product.categories.add(non_primary_category1, non_primary_category2)

                self.stdout.write(self.style.SUCCESS(f'Product "{new_product}" created with gallery "{gallery}"'))

        self.stdout.write(self.style.SUCCESS(f'"{Product.objects.count()}" Product records created'))
