from django.contrib import admin

from .models import CommunityVoice, EventConversation, FeaturedEdition, LandingContent, Newsletter, Waitlist

admin.site.register((Waitlist, FeaturedEdition, CommunityVoice, EventConversation, Newsletter))


@admin.register(LandingContent)
class LandingContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'is_published', 'display_order', 'published_at')
    list_filter = ('section', 'is_published')
    search_fields = ('title', 'description', 'author', 'tags')
    list_editable = ('is_published', 'display_order')
