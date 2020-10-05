from django.core.management.base import BaseCommand
from common.models import Tag

class Command(BaseCommand):
    help = 'Create start tags/intentions'

    def handle(self, *args, **options):
        print('Seeding tags')
        tag_data = (
            # ('Extreme weather report',
            # 'Resilience project',
            # 'Climate justice event',
            # 'Organization profile',
            # 'Water well needed',
            ('Cyclone', 'report_type'),
            ('Drought', 'report_type'),
            ('Flood/Landslide', 'report_type'),
            ('Heat wave', 'report_type'),
            ('Crop loss', 'report_impact'),
            ('Food insecurity', 'report_impact'),
            ('Water scarcity', 'report_impact'),
            ('Homelessness', 'report_impact'),
            ('Loss of livelihood', 'report_impact'),
        )
        for tag_datum in tag_data:
            Tag.objects.get_or_create(
                name=tag_datum[0],
                is_starter=True,
                type=tag_datum[1],
            )
