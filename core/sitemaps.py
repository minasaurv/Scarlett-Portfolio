from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return ['core:index', 'core:portfolio']

    def location(self, item):
        return reverse(item)