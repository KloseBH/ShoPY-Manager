from django.contrib import admin
from marketplaces.models import Marketplace

class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'key', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

admin.site.register(Marketplace, MarketplaceAdmin)

