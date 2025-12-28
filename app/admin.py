from django.contrib import admin
from .models import ShortLink

# Register your models here.
# admin.site.register(ShortLink)

@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'created_at')
    search_fields = ('original_url', 'short_code')
    readonly_fields = ('created_at',)