from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include, re_path
from django.views.static import serve

from core.sitemaps import StaticViewSitemap
from core import views

sitemaps = {'static': StaticViewSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('core.urls')),
    # Serve uploaded images directly (production files live on the Railway volume)
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
