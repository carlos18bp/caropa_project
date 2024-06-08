from faker import Faker
from django.core.management.base import BaseCommand
from django.core.files import File
from caropa_app.models import Product, ProductDetail, Category, Size, Color, ProductByRef
from django_attachments.models import Library, Attachment
import random
import os

class Command(BaseCommand):
    help = 'Create Product records in the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_products', type=int, nargs='?', default=10)

    def handle(self, *args, **options):
        number_of_products = options['number_of_products']
        fake = Faker()

        # List of test images
        test_images = [
            '/media/temp/product_temp1.jpg',
            '/media/temp/product_temp2.jpg',
            '/media/temp/product_temp3.jpg',
            '/media/temp/product_temp4.jpg',
        ]

        # List of predefined colors and sizes
        predefined_colors = ['RED', 'BLUE', 'YELLOW', 'GREEN', 'ORANGE', 'PURPLE', 'BLACK', 'WHITE', 'PINK', 'BROWN']
        predefined_sizes = ['S', 'M', 'L', 'XL']

        # Ensure the test images exist
        for image_path in test_images:
            if not os.path.isfile(os.getcwd() + image_path):
                self.stdout.write(self.style.ERROR(f'Image file {image_path} not found'))
                return

        for _ in range(number_of_products):
            # Create or get a ProductByRef
            ref_value = 'REF' + str(random.randint(1000, 9999))
            product_by_ref, _ = ProductByRef.objects.get_or_create(ref=ref_value)

            # Create a new ProductDetail
            product_detail = ProductDetail.objects.create(
                name=fake.word(),
                description=fake.text(max_nb_chars=300),
                price=fake.pydecimal(left_digits=4, right_digits=2, positive=True)
            )

            # Create or get a random Category
            category, _ = Category.objects.get_or_create(name=fake.word())

            # Select a random predefined size
            size, _ = Size.objects.get_or_create(name=random.choice(predefined_sizes))

            # Select a random predefined color
            color, _ = Color.objects.get_or_create(name=random.choice(predefined_colors))

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

            # Now create the product with the gallery
            new_product = Product.objects.create(
                ref=product_by_ref,
                product_detail=product_detail,
                size=size,
                color=color,
                gallery=gallery  # Associate the gallery with the product
            )

            # Add the category to the product
            new_product.categories.add(category)

            self.stdout.write(self.style.SUCCESS(f'Product "{new_product}" created with gallery "{gallery}"'))

        self.stdout.write(self.style.SUCCESS(f'"{Product.objects.count()}" Product records created'))
