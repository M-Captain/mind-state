from django.contrib import messages
from django.conf import settings
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from pathlib import Path
from .community import COMMUNITY_MEMBERS
from .models import CommunityVoice, EventConversation, FeaturedEdition, LandingContent, Newsletter, Waitlist


def contribute(request):
	content_dir = Path(settings.BASE_DIR) / 'templates'
	return render(request, 'contribute.html', {
		'full_guidelines': mark_safe((content_dir / 'contribute-full.html').read_text(encoding='utf-8')),
		'brief_guidelines': mark_safe((content_dir / 'contribute-brief.html').read_text(encoding='utf-8')),
		'guidelines_toc': mark_safe((content_dir / 'contribute-toc.html').read_text(encoding='utf-8')),
	})


@login_required
def home(request):
	if request.method == 'POST':
		name = request.POST.get('name', '').strip()
		email = request.POST.get('email', '').strip()
		if email:
			Waitlist.objects.get_or_create(email=email, defaults={'name': name})
			messages.success(request, 'You have been added to the waitlist.')
		return redirect('home')

	content = LandingContent.objects.filter(is_published=True)
	latest_articles = list(content.filter(section=LandingContent.ARTICLES).order_by('-published_at', 'display_order')[:2])
	latest_art = list(content.filter(section=LandingContent.ART).order_by('-published_at', 'display_order')[:2])
	recently_added = []
	for index in range(max(len(latest_articles), len(latest_art))):
		for group in [latest_articles, latest_art]:
			if index < len(group):
				recently_added.append(group[index])
	pick_ids = [1005, 2006, 1008]
	picks = content.in_bulk(pick_ids)
	return render(request, 'home.html', {
		'articles': content.filter(section=LandingContent.ARTICLES)[:12],
		'landing_events': content.filter(section=LandingContent.EVENTS)[:3],
		'recently_added': recently_added,
		'editor_picks': [picks[pk] for pk in pick_ids if pk in picks],
		'artworks': content.filter(section=LandingContent.ART),
		'community_voices': CommunityVoice.objects.filter(is_published=True)[:3],
	})

@login_required
def article(request, pk):
	content = get_object_or_404(
		LandingContent,
		pk=pk,
		is_published=True,
	)
	other_content = LandingContent.objects.filter(is_published=True).exclude(pk=content.pk)
	related_articles = list(other_content.filter(
		section=content.section,
	)[:2]) + list(other_content.exclude(section=content.section)[:2])
	community_voices = CommunityVoice.objects.filter(is_published=True)[:3]
	return render(request, 'article.html', {
		'article': content,
		'related_articles': related_articles,
		'community_voices': community_voices,
	})

@login_required
def search(request):
	query = request.GET.get('q', '').strip()
	results = LandingContent.objects.filter(
		is_published=True,
		section__in=[LandingContent.ARTICLES, LandingContent.ART],
	)
	section = request.GET.get('section', '')
	if section in [LandingContent.ARTICLES, LandingContent.ART]:
		results = results.filter(section=section)
	if query:
		results = results.filter(
			Q(title__icontains=query)
			| Q(description__icontains=query)
			| Q(author__icontains=query)
			| Q(tags__icontains=query)
		)
	return render(request, 'search.html', {
		'search_query': query,
		'search_results': results,
		'search_section': section,
	})


@login_required
def community_directory(request):
	ordered_members = sorted(COMMUNITY_MEMBERS, key=lambda member: member['name'].casefold())
	grouped_members = {}
	for member in ordered_members:
		letter = member['name'][0].upper()
		grouped_members.setdefault(letter, []).append(member)

	return render(request, 'community-directory.html', {
		'community_members': COMMUNITY_MEMBERS,
		'member_groups': [
			{'letter': letter, 'members': members}
			for letter, members in grouped_members.items()
		],
		'member_count': len(ordered_members),
		'alphabet': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
		'available_letters': set(grouped_members),
	})

@login_required
def art_post(request, slug):
	content = get_object_or_404(LandingContent, section=LandingContent.ART,
		link_url=f'/app/art/{slug}/', is_published=True)
	return article(request, content.pk)

@login_required
def landing(request):
	if request.method == 'POST':
		name = request.POST.get('name', '').strip()
		email = request.POST.get('email', '').strip()
		if email:
			Waitlist.objects.get_or_create(email=email, defaults={'name': name})
			messages.success(request, 'You have been added to the waitlist.')
		return redirect('landing')

	return render(request, 'landing.html', {
		'featured_editions': FeaturedEdition.objects.filter(is_published=True),
		'community_voices': CommunityVoice.objects.filter(is_published=True),
		'events_conversations': EventConversation.objects.filter(is_published=True),
		'newsletters': Newsletter.objects.filter(is_published=True),
	})
