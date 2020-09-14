from django.core.management.base import BaseCommand
from common.models import Tag

class Command(BaseCommand):
    help = 'Create start tags/intentions'
    
    def handle(self, *args, **options):
        names = (
            'Extreme weather report',
            'Resilience project',
            'Climate justice event',
            'Organization profile',
            'Water well needed',
        )
        for name in names:
            Tag.objects.get_or_create(name=name, is_starter=True)
