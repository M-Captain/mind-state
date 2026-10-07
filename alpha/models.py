from django.db import models


class Waitlist(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.email


class FeaturedEdition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    link_url = models.URLField(blank=True)
    published_at = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('display_order', '-published_at', '-id')

    def __str__(self):
        return self.title


class CommunityVoice(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author_name = models.CharField(max_length=120)
    author_role = models.CharField(max_length=160, blank=True)
    image_url = models.URLField(blank=True)
    link_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('display_order', '-id')

    def __str__(self):
        return self.title


class EventConversation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True)
    image_url = models.URLField(blank=True)
    registration_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ('event_date',)

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    issue_date = models.DateField(blank=True, null=True)
    image_url = models.URLField(blank=True)
    issue_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ('-issue_date', '-id')

    def __str__(self):
        return self.title


class LandingContent(models.Model):
    ARTICLES = 'articles'
    EVENTS = 'events'
    TOP_PICKS = 'top_picks'
    ART = 'art'
    SECTION_CHOICES = (
        (ARTICLES, 'Articles'),
        (EVENTS, 'Events'),
        (TOP_PICKS, "Editor's Top Picks"),
        (ART, 'Art'),
    )

    section = models.CharField(max_length=16, choices=SECTION_CHOICES, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=120, blank=True)
    published_at = models.DateField(blank=True, null=True)
    image_url = models.URLField(blank=True)
    link_url = models.URLField(blank=True)
    tags = models.CharField(max_length=255, blank=True, help_text='Comma-separated labels shown on the card.')
    is_published = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('display_order', '-published_at', '-id')

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
