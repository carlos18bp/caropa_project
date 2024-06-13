from django.core.management.base import BaseCommand
from caropa_app.models import Banner
from faker import Faker

class Command(BaseCommand):
    help = 'Create Banner records in the database'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(4):
            banner_text = fake.sentence(nb_words=6)
            banner_instance = Banner.objects.create(text=banner_text)
            self.stdout.write(self.style.SUCCESS(f'Banner "{banner_instance}" created'))

        self.stdout.write(self.style.SUCCESS(f'4 Banner records created'))
