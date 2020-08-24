from django.contrib import admin
from core.models import UrlMapping

class UrlMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin_url', 'dest_url')

admin.site.register(UrlMapping, UrlMappingAdmin)