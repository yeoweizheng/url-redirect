from django.urls import re_path

from .views import UrlRedirectView

app_name = 'core'
urlpatterns = [
    re_path(r'^(?P<origin_url>.*)$', UrlRedirectView.as_view(), name='redirect-view')
]
