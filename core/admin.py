from django.contrib import admin
from django.utils.html import format_html

from .models import PortfolioItem

admin.site.site_header = "Scarlett's Portfolio Manager"
admin.site.site_title = 'Portfolio Manager'
admin.site.index_title = 'Manage your portfolio'


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'category', 'year', 'is_featured', 'order', 'is_published')
    list_display_links = ('thumbnail', 'title')
    list_editable = ('is_featured', 'order', 'is_published')
    list_filter = ('is_published', 'is_featured', 'category', 'year')
    search_fields = ('title', 'description', 'category', 'client', 'tools')
    readonly_fields = ('image_preview',)
    save_on_top = True
    actions = ('publish', 'unpublish')

    fieldsets = (
        ('The piece', {
            'description': 'Give your piece a name, a short description and an image.',
            'fields': ('title', 'description', 'image', 'image_alt', 'image_preview'),
        }),
        ('Details', {
            'description': 'All optional. These show up under the piece on your portfolio page.',
            'fields': ('category', 'client', 'year', 'tools'),
        }),
        ('Optional link', {
            'description': 'Add a link (for example to the live project) and the image will open it in a new tab.',
            'fields': ('link', 'link_text'),
        }),
        ('Display', {
            'description': 'Featured pieces appear first. Then lower numbers appear first. Untick "Is published" to hide a piece without deleting it.',
            'fields': ('is_featured', 'order', 'is_published'),
        }),
    )

    @admin.display(description='Preview')
    def thumbnail(self, obj):
        if not obj.image:
            return '-'
        return format_html(
            '<img src="{}" alt="" style="height:56px;width:80px;object-fit:cover;border-radius:6px">',
            obj.image.url,
        )

    @admin.display(description='Current image')
    def image_preview(self, obj):
        if not obj.image:
            return 'No image yet. Choose one above and save to see it here.'
        return format_html(
            '<img src="{}" alt="" style="max-width:320px;max-height:240px;border-radius:8px">',
            obj.image.url,
        )

    @admin.action(description='Show selected pieces on the site')
    def publish(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'{count} piece(s) are now visible.')

    @admin.action(description='Hide selected pieces from the site')
    def unpublish(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'{count} piece(s) are now hidden.')
