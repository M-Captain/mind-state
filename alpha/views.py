from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import CommunityVoice, EventConversation, FeaturedEdition, LandingContent, Newsletter, Waitlist


def home(request):
	if request.method == 'POST':
		name = request.POST.get('name', '').strip()
		email = request.POST.get('email', '').strip()
		if email:
			Waitlist.objects.get_or_create(email=email, defaults={'name': name})
			messages.success(request, 'You have been added to the waitlist.')
		return redirect('home')

	content = LandingContent.objects.filter(is_published=True)
	return render(request, 'home.html', {
		'articles': content.filter(section=LandingContent.ARTICLES)[:8],
		'landing_events': content.filter(section=LandingContent.EVENTS)[:3],
		'editor_picks': content.filter(section=LandingContent.TOP_PICKS)[:3],
		'artworks': content.filter(section=LandingContent.ART)[:3],
		'community_voices': CommunityVoice.objects.filter(is_published=True)[:3],
	})


def article(request, pk):
	content = get_object_or_404(
		LandingContent,
		pk=pk,
		section=LandingContent.ARTICLES,
		is_published=True,
	)
	related_articles = LandingContent.objects.filter(
		section=LandingContent.ARTICLES,
		is_published=True,
	).exclude(pk=content.pk)[:4]
	community_voices = CommunityVoice.objects.filter(is_published=True)[:3]
	return render(request, 'article.html', {
		'article': content,
		'related_articles': related_articles,
		'community_voices': community_voices,
	})


def search(request):
	query = request.GET.get('q', '').strip()
	results = LandingContent.objects.filter(
		is_published=True,
		section=LandingContent.ARTICLES,
	)
	if query:
		results = results.filter(
			Q(title__icontains=query)
			| Q(description__icontains=query)
			| Q(author__icontains=query)
			| Q(tags__icontains=query)
		)
	return render(request, 'search.html', {
		'search_query': query,
		'search_results': results[:12],
	})


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
