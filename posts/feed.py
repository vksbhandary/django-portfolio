from django.contrib.syndication.views import Feed

from django.template.defaultfilters import truncatewords

from .models import Post
from django.utils import feedgenerator
from django.utils.html import strip_tags

class CorrectMimeTypeFeed(feedgenerator.DefaultFeed):
    content_type = 'application/xml; charset=utf-8'

class PostsFeed(Feed):
    title = 'Blog Feeds'
    link = '/blog/'
    description = 'Latest Blog Posts'
    feed_type = CorrectMimeTypeFeed

    def items(self):
        return Post.objects.filter(status='published').order_by('-created')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(strip_tags(item.content), 20)

    def item_link(self, item):
        return item.get_absolute_url()