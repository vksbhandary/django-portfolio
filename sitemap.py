# sitemap.py

from django.contrib.sitemaps import Sitemap
# from .models import Post
from django.urls import reverse

class SiteSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return [ 
        '/',
        '/about/',
         '/project/',
         '/blog/'
         ]

    def location(self, item):
        return item
