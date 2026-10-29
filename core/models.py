from django.db import models


class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/', blank=True)
    image_alt = models.CharField(
        max_length=200, blank=True,
        help_text='Describe the image for people using screen readers. Defaults to the title.',
    )
    category = models.CharField(max_length=80, blank=True, help_text='For example: Logo, Illustration, Branding.')
    client = models.CharField(max_length=120, blank=True)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    tools = models.CharField(max_length=200, blank=True, help_text='For example: Photoshop, Procreate.')
    link = models.URLField(blank=True)
    link_text = models.CharField(
        max_length=60, blank=True,
        help_text='Text on the link button, for example "View live site". Defaults to "Visit project".',
    )
    is_featured = models.BooleanField(default=False, help_text='Featured pieces are shown first and highlighted.')
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'order', '-created_at']

    @property
    def tool_list(self):
        return [t.strip() for t in self.tools.split(',') if t.strip()]

    def __str__(self):
        return self.title
