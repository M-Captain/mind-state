"""Import the six supplied visual art posts without replacing articles."""
import json
from pathlib import Path
from django.conf import settings
from django.core import serializers
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


class Command(BaseCommand):
    help = 'Validate six art posts and 30 images; --install imports them.'

    def add_arguments(self, parser):
        parser.add_argument('--install', action='store_true')

    def handle(self, *args, **options):
        root = Path(settings.BASE_DIR)
        posts = json.loads((root/'content/art-library.json').read_text(encoding='utf-8'))
        if len(posts) != 6:
            raise CommandError('Expected six art posts.')
        for post in posts:
            if len(post['images']) != 5:
                raise CommandError('Each art post must contain five images.')
            for image in post['images']:
                path = root/image['src'].lstrip('/')
                if not path.is_file() or path.stat().st_size != image['bytes']:
                    raise CommandError(f'Missing or changed art image: {path}')
            for folder in ['article-content', 'article-credits']:
                if not (root/f'templates/{folder}/{post["id"]}.html').is_file():
                    raise CommandError('Missing art detail template.')
        if options['install']:
            fixture = (root/'content/art-posts.fixture.json').read_text(encoding='utf-8')
            with transaction.atomic():
                for item in serializers.deserialize('json', fixture):
                    item.save()
            self.stdout.write(self.style.SUCCESS('Imported six art posts; existing articles preserved.'))
        else:
            self.stdout.write('Validated six art posts and 30 images. Use --install to import.')
