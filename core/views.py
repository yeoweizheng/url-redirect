from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.http import Http404
from urllib.parse import quote
from .models import UrlMapping

class UrlRedirectView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        origin_url = quote(kwargs['origin_url'])
        try:
            url_mapping = UrlMapping.objects.get(origin_url=origin_url)
            return url_mapping.dest_url
        except UrlMapping.DoesNotExist:
            raise Http404('Page not found.')