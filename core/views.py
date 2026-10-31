from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import PortfolioItem


def robots_txt(request):
    sitemap_url = request.build_absolute_uri(
        reverse('django.contrib.sitemaps.views.sitemap')
    )
    return HttpResponse(
        f'User-agent: *\nAllow: /\nSitemap: {sitemap_url}\n',
        content_type='text/plain',
    )


def index(request):
    return render(request, 'core/index.html')


def portfolio(request):
    items = PortfolioItem.objects.filter(is_published=True)
    return render(request, 'core/portfolio.html', {'items': items})
