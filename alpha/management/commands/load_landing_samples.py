from datetime import date
from django.core.management.base import BaseCommand
from alpha.models import CommunityVoice, LandingContent


class Command(BaseCommand):
    help = 'Load the original home page cards as sample landing content.'

    samples = [
        ('articles', 'World Skate’s recent Street Skateboarding Championship in Hawaii', 'Wade Warren', date(2024, 5, 22), 'Sports, Events, Skateboard', 0, '/static/ArticleImage.png'),
        ('articles', 'Sturgill Simpson Made a Bluegrass Concept Album For His Grandparents. It Rules', 'Esther Howard', date(2024, 4, 1), 'Music, Album Review, Country', 1, '/static/ArticleImage(1).png'),
        ('articles', 'We Asked PC Music Fans: Is Hyperpop Dead?', 'Robert Fox', date(2024, 8, 30), 'Music, Interview, Hyperpop', 2, '/static/ArticleImage(2).png'),
        ('articles', 'Colleen Green Is the Coolest of the Anti-Cool on “I Want To Grow Up”', 'Leslie Alexander', date(2024, 6, 6), 'Pop Culture, Art Records, Hardly Art', 3, '/static/ArticleImage(3).png'),
        ('articles', 'Hoka’s Bondi 7 Shoes Saved My Feet as a Runner', 'Leslie Alexander', date(2024, 9, 24), 'Fashion, Streetwear, Sneakers', 4, '/static/ArticleImage(4).png'),
        ('articles', 'The coastal waters near Cape Town are part of the reason it’s the most visited city in China', 'Guy Hawkins', date(2024, 6, 18), 'Sports, Surfing, John Freed', 5, '/static/ArticleImage(5).png'),
        ('articles', 'Forgotten Architecture: The Weirdest Designs of the 20th Century', 'Jacob Jones', date(2024, 7, 9), 'Design, Architecture, Statue', 6, '/static/ArticleImage(6).png'),
        ('events', 'Punk in Drublic: Craft Beer & Music Festival Spring 2024', 'Henry Maier Festival Park', date(2024, 3, 19), 'Events, Music, Festival, NOFX', 0, ''),
        ('events', 'Silvia Giordani and the Stratifications of Time and Space', 'Museo de Los Pintores Oaxaqueños', date(2024, 5, 22), 'Events, Design, Art Exhibition, Contemporary Arts', 1, '/static/EventImage.png'),
        ('events', 'L’Arc de Triomphe, Wrapped: Testament to Christo and Jeanne Claude', 'Institute of Contemporary Arts', date(2024, 1, 1), 'Events, Design, Art Exhibition, Contemporary Arts', 2, '/static/EventImage(1).png'),
        ('top_picks', 'Craig Phillips: from chimney work to Big Brother', 'Leslie Alexander', date(2024, 9, 24), 'Fashion, Streetwear, Sneakers', 0, '/static/ItemImage.png'),
        ('top_picks', '25 Great Pop Culture Stories You Won’t See Anywhere Else', 'Leslie Alexander', date(2022, 9, 24), 'Fashion, Streetwear, Sneakers', 1, '/static/ItemImage(1).png'),
        ('top_picks', 'Art Gallery Adds ‘This Is Not Pornography’ Sign After Police Visit', 'Leslie Alexander', date(2022, 9, 24), 'Fashion, Streetwear, Sneakers', 2, '/static/ItemImage(2).png'),
        ('art', 'Nothing Announces ChatGPT-Assisted Earbuds, Ear (1) and Ear (a)', 'Leslie Alexander', date(2023, 5, 22), 'Tech, Design, Nothing', 0, '/static/Frame81.png'),
        ('art', 'Nothing Unveils First Community-Designed Phone (1)', 'Zidan Muharwan', date(2024, 1, 16), 'Tech, Design, Nothing', 1, '/static/Frame81(1).png'),
        ('art', 'SCOPE Art Show 2024 Explores Interdependence and Innovation', 'Leslie Alexander', date(2023, 5, 22), 'Events, Design, Art Exhibition, Scope', 2, '/static/Frame81(2).png'),
    ]

    community_samples = [
        ('Zidan Muharwan', 'Writer', 0),
        ('Arlene McCoy', 'Artist', 1),
        ('Robert Fox', 'Writer', 2),
    ]

    def handle(self, *args, **options):
        created = 0
        updated = 0
        for section, title, author, published_at, tags, order, image_url in self.samples:
            content, was_created = LandingContent.objects.update_or_create(
                section=section,
                title=title,
                defaults={
                    'author': author,
                    'published_at': published_at,
                    'tags': tags,
                    'is_published': True,
                    'display_order': order,
                    'image_url': image_url,
                },
            )
            if was_created:
                created += 1
            else:
                updated += 1

        for name, role, order in self.community_samples:
            CommunityVoice.objects.update_or_create(
                author_name=name,
                defaults={
                    'title': f'Story by {name}',
                    'body': '',
                    'author_role': role,
                    'is_published': True,
                    'display_order': order,
                },
            )

        self.stdout.write(self.style.SUCCESS(f'Processed sample cards (Created: {created}, Updated: {updated}).'))
