import os
from django.core.files import File
from django.core.management.base import BaseCommand
from django_attachments.models import Attachment, Library
from caropa_app.models import Home
from faker import Faker

class Command(BaseCommand):
    help = 'Create Home records in the database'

    def handle(self, *args, **options):
        fake = Faker()

        # List of test images
        test_images = [
            # carousel_presentation content
            '/media/temp/home/carousel_presentation/image_temp1.webp',
            '/media/temp/home/carousel_presentation/image_temp2.webp',
            '/media/temp/home/carousel_presentation/image_temp3.webp',
            '/media/temp/home/carousel_presentation/image_temp4.webp',
            # section_3_gallery content
            '/media/temp/home/section_3/image_temp1.webp',
            '/media/temp/home/section_3/image_temp2.webp',
            '/media/temp/home/section_3/image_temp3.webp',
            # section_5_image content
            '/media/temp/home/image_temp1.webp',
        ]

        # Ensure the test images exist
        for image_path in test_images:
            if not os.path.isfile(os.getcwd() + image_path):
                self.stdout.write(self.style.ERROR(f'Image file {image_path} not found'))
                return

        # Create the gallery for carousel_presentation
        carousel_gallery = Library.objects.create(title=fake.word())
        for image_path in test_images[:4]:  # Use first 4 images for carousel
            image_path = os.getcwd() + image_path
            with open(image_path, 'rb') as image_file:
                Attachment.objects.create(
                    library=carousel_gallery,
                    file=File(image_file, name=os.path.basename(image_path)),
                    original_name=os.path.basename(image_path),
                    rank=0
                )

        # Create the gallery for section_3_gallery
        section_3_gallery = Library.objects.create(title=fake.word())
        for image_path in test_images[4:7]:  # Use next 3 images for section 3
            image_path = os.getcwd() + image_path
            with open(image_path, 'rb') as image_file:
                Attachment.objects.create(
                    library=section_3_gallery,
                    file=File(image_file, name=os.path.basename(image_path)),
                    original_name=os.path.basename(image_path),
                    rank=0
                )

        # Create the home instance
        home_instance = Home.objects.create(
            carousel_presentation=carousel_gallery,
            section_3_title=fake.sentence(nb_words=5),
            section_3_description=fake.text(max_nb_chars=200),
            section_3_gallery=section_3_gallery,
            section_5_title=fake.sentence(nb_words=5),
            section_5_description=fake.text(max_nb_chars=200),
            section_5_image=File(open(os.getcwd() + test_images[7], 'rb'), name=os.path.basename(test_images[7]))
        )

        self.stdout.write(self.style.SUCCESS(f'Home instance "{home_instance}" created'))
