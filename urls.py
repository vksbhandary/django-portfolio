# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
import posts
from django.contrib import admin
from django.urls import path

from sitemap import SiteSitemap

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from posts.models import Post
sitemaps = {
    'static': SiteSitemap,
}
blog_dict = {
    'queryset': Post.objects.filter(status='published'),
    'date_field': 'modified',
}

handler404 = 'posts.views.handler404'


urlpatterns = [
	path('sitemap.xml', sitemap, {'sitemaps': {'static':SiteSitemap,'blog': GenericSitemap(blog_dict, priority=0.6)} },
         name='django.contrib.sitemaps.views.sitemap'),
	path('admin/', admin.site.urls),
    url('summernote/', include('django_summernote.urls')),
	url(r'^', include("posts.urls")),
    # add your own patterns here
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
    
)
