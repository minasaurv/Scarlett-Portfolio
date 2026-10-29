from django.shortcuts import render

from .models import PortfolioItem


def index(request):
    return render(request, 'core/index.html')


def portfolio(request):
    items = PortfolioItem.objects.filter(is_published=True)
    return render(request, 'core/portfolio.html', {'items': items})
