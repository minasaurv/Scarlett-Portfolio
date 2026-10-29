from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # Serve uploaded images directly (fine for a small portfolio; files live on the Railway volume)
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
