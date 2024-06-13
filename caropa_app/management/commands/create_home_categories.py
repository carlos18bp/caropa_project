import os
from django.core.files import File
from django.core.management.base import BaseCommand
from caropa_app.models import HomeCategory

class Command(BaseCommand):
    help = 'Create HomeCategory records in the database'

    def handle(self, *args, **options):
        home_category_titles = [
            'Just in', 
            'A fresh style', 
            'Deluxe', 
            'New season essentials', 
            'New western', 
            'Sun-kissed swimwear', 
            'Works day', 
            'Dressed for date night', 
            'All dressed up', 
            'The spring style refresh', 
            'New season', 
            'A fresh day'
        ]

        # List of test images
        test_images = [
            '/media/temp/home/category/image_temp1.webp',
            '/media/temp/home/category/image_temp2.webp',
            '/media/temp/home/category/image_temp3.webp',
            '/media/temp/home/category/image_temp4.webp',
            '/media/temp/home/category/image_temp5.webp',
            '/media/temp/home/category/image_temp6.webp',
            '/media/temp/home/category/image_temp7.webp',
            '/media/temp/home/category/image_temp8.webp',
            '/media/temp/home/category/image_temp9.webp',
            '/media/temp/home/category/image_temp10.webp',
            '/media/temp/home/category/image_temp11.webp',
            '/media/temp/home/category/image_temp12.webp',
        ]

        # Ensure the test images exist
        for image_path in test_images:
            if not os.path.isfile(os.getcwd() + image_path):
                self.stdout.write(self.style.ERROR(f'Image file {image_path} not found'))
                return

        for i, title in enumerate(home_category_titles):
            image_path = os.getcwd() + test_images[i]
            with open(image_path, 'rb') as image_file:
                home_category = HomeCategory.objects.create(
                    title=title,
                    image=File(image_file, name=os.path.basename(image_path))
                )
                self.stdout.write(self.style.SUCCESS(f'HomeCategory "{home_category.title}" created'))

        self.stdout.write(self.style.SUCCESS(f'{len(home_category_titles)} HomeCategory records created'))
