from django.db import models

class UrlMapping(models.Model):
    origin_url = models.CharField(max_length=2048)
    dest_url = models.CharField(max_length=2048)