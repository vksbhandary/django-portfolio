# Create your models here.
from django.db import models

# Create your models here.
# from common.models import IndexedTimeStampedModel, SluggedModel, get_uniqueslug, get_random_string
from django.template.defaultfilters import slugify
import string
import random
from django.urls import reverse
from django.db.models.signals import m2m_changed
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

DEFINED_POST_STATUS = (
        ('draft','Draft'),
        ('published','Published'),
        ('trash','Trash'),
        )

SLUG_OPTIONS = {
    ('tag','Tag'),
    ('post','Post'),
}

def get_random_string(N=10):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(N))


def get_uniqueslug(model,title):
    slug = slugify(title)
    if slug == "":
        return "--{}".format(get_random_string(20))
    unique_slug = slug
    num = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug


class IndexedTimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True,verbose_name =_('created'))
    modified = models.DateTimeField(auto_now=True,verbose_name =_('modified'), db_index=True)

    class Meta:
        abstract = True


class SluggedModel(IndexedTimeStampedModel):
    class Meta:
        abstract = True
    slug = models.SlugField(unique=True)


class Tag(SluggedModel):
    title= models.CharField(max_length=50,unique=True, verbose_name = "Tag name")
    count =  models.PositiveIntegerField(default=0,verbose_name = "Post Counts")

    def get_absolute_url(self):
        return "/tag/"+self.slug

    def save(self,*args, **kwargs):
        slug = get_uniqueslug(Tag,self.title)
        # if its new record
        if self.pk is None:
            self.slug = slug
        # if title got changed
        if slugify(self.title) not in self.slug and (not slugify(self.title) == ""):
            self.slug = slug

        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(SluggedModel):
    class Meta:
        verbose_name_plural = "Posts"
        verbose_name = "Post"
    title = models.CharField(max_length=250,unique=True, verbose_name = "Post title")
    content = models.TextField(verbose_name = "Post Content")
    summary = models.CharField(max_length=125, blank=True, default=None, null=True,verbose_name = "Post summary")
    status = models.CharField(max_length=25, choices =DEFINED_POST_STATUS, default = 'draft', verbose_name = "Status")
    tag = models.ManyToManyField(Tag,blank=True, related_name ='post_tag', verbose_name = "Post Tags")
    author = models.ForeignKey(User, on_delete=models.CASCADE ,related_name ='post_author', verbose_name = "Author")
    keywords = models.CharField(max_length=512,blank=True, default=None, null=True, verbose_name = "SEO keywords")
    published = models.DateTimeField(blank=True, default=None, null=True, verbose_name = "Published at")
    featuredimage = models.ImageField(upload_to='featured/%Y/%m/%d', verbose_name = "featured image",blank=True, default=None, null=True)
    featuredurl = models.URLField(max_length=1024, verbose_name = "featured image url",blank=True,default=None, null=True)
    featuredthumburl = models.URLField(max_length=1024, verbose_name = "featured thumbnail url",blank=True,default=None, null=True)


    def get_absolute_url(self):
        return "/blog/"+self.slug

    def __str__(self):
            return self.title
    def save(self , *args, **kwargs):
        slug = get_uniqueslug(Tag,self.title)

        # if the record being saved is new?
        if self.pk is None:
            self.slug = slug
        # if title got changed
        if slugify(self.title) not in self.slug and (not slugify(self.title) == ""):
            self.slug = slug

        print(self.published)
        if self.published is None and self.status == 'published':
            self.published = datetime.utcnow()

        super(Post, self).save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

def tags_changed(sender, instance, action,  **kwargs):
    if action =='post_add':
        for tag in list(instance.tag.all()):
            tagobj = Tag.objects.get(id=tag.id)
            total = Post.objects.filter(tag = tagobj).count()
            tagobj.count = total
            tagobj.save()

m2m_changed.connect(tags_changed, sender=Post.tag.through)

class Subscriber(models.Model):
    class Meta:
        verbose_name_plural = "Subscribers"
        verbose_name = "Subscriber"

    name = models.CharField(max_length=250,blank=True, default=None, null=True, verbose_name = "Full name")
    email = models.EmailField(max_length=254,unique=True, verbose_name = "Email", error_messages={'unique':"This User has already subscribed to our updates."})
    subscribed = models.BooleanField(default=True ,verbose_name = "Subscribed")
    code = models.CharField(max_length=256, unique=True, verbose_name = "Unsubsribe code")
    verified = models.BooleanField(default=False ,verbose_name = "Email verified subscriber")
    
    def save(self , *args, **kwargs):
        self.code = get_random_string(50)
        super(Subscriber, self).save(*args, **kwargs)


class PostSettings(models.Model):
    class Meta:
        verbose_name = "Post setting"
        
    default_thumb = models.URLField(max_length=1024, verbose_name = "Default featured thumbnail",blank=True,default=None, null=True)
    default_featured = models.URLField(max_length=1024, verbose_name = "Default featured image",blank=True,default=None, null=True)
    
    
