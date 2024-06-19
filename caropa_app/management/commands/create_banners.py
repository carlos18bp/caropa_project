from django.core.management.base import BaseCommand
from caropa_app.models import Banner
from faker import Faker

class Command(BaseCommand):
    help = 'Create Banner records in the database'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(5):
            banner_text = fake.sentence(nb_words=6)
            banner_text_en = banner_text + ' (EN)'
            banner_text_es = banner_text + ' (ES)'
            banner_instance = Banner.objects.create(text_en=banner_text_en, text_es=banner_text_es)
            self.stdout.write(self.style.SUCCESS(f'Banner "{banner_instance}" created'))

        self.stdout.write(self.style.SUCCESS('5 Banner records created'))
