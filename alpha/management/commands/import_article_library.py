"""Install the supplied editorial library using existing content fields."""
import hashlib
import json
from pathlib import Path

from django.conf import settings
from django.core import serializers
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from alpha.models import LandingContent


class Command(BaseCommand):
    help = 'Validate and import the 11 supplied articles; --replace-demos replaces existing content.'

    def add_arguments(self, parser):
        parser.add_argument('--replace-demos', action='store_true')

    def handle(self, *args, **options):
        root = Path(settings.BASE_DIR)
        records = json.loads((root/'content/article-library.json').read_text(encoding='utf-8'))
        fixture = root/'content/articles.fixture.json'
        if len(records) != 11:
            raise CommandError('Expected exactly 11 supplied articles.')
        for record in records:
            source = root/'content/source_articles'/record['source_document']
            if hashlib.sha256(source.read_bytes()).hexdigest() != record['source_sha256']:
                raise CommandError(f"Source changed: {source.name}")
            if not (root/f"templates/article-content/{record['id']}.html").is_file():
                raise CommandError('Missing reading-page content.')
            if len(record['images']) != 5 or any(not (root/image['src'].lstrip('/')).is_file() for image in record['images']):
                raise CommandError('Missing article images.')
        if not options['replace_demos']:
            self.stdout.write('Validated 11 articles and 55 images. Use --replace-demos to install.')
            return
        backup = root/'work/demo-articles-before-import.json'
        backup.parent.mkdir(exist_ok=True)
        if not backup.exists():
            backup.write_text(serializers.serialize('json', LandingContent.objects.all(), ensure_ascii=False), encoding='utf-8')
        with transaction.atomic():
            LandingContent.objects.exclude(pk__range=(2001, 2006)).delete()
            for item in serializers.deserialize('json', fixture.read_text(encoding='utf-8')):
                item.save()
        self.stdout.write(self.style.SUCCESS('Imported 11 articles; demo content removed. Other database records preserved.'))
