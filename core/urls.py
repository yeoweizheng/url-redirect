from django.urls import re_path

from .views import UrlRedirectView

app_name = 'core'
urlpatterns = [
    re_path(r'^(?P<origin_url>[a-zA-Z0-9\/.% ]+)$', UrlRedirectView.as_view(), name='redirect-view')
]
