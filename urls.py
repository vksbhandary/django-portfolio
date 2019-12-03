# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
import posts
from django.contrib import admin
from django.urls import path


urlpatterns = [
	path('admin/', admin.site.urls),
    url('summernote/', include('django_summernote.urls')),
	url(r'^', include("posts.urls")),
    # add your own patterns here
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
    
)
