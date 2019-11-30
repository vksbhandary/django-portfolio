from django.db import models
from django.contrib.auth.models import User

from posts.models import IndexedTimeStampedModel

# Create your models here.
URL_TYPE = {
    ('medium','Medium'),
    ('linkedin','LinkedIn'),
    ('facebook','Facebook'),
    ('twitter','Twitter'),
    ('github','Github'),
    ('pintrest','Pintrest'),
}


class SocialURL(models.Model):
    class Meta:
        verbose_name_plural = "Social Url"
        verbose_name = "Social Url"
    type = models.CharField(max_length=25, choices =URL_TYPE, default = 'other', verbose_name = "URL Type")
    link = models.URLField(max_length=1024,blank=True, default=None, null=True, verbose_name="URL")
    def __str__(self):
        return self.link


class UserProfile(IndexedTimeStampedModel):
    class Meta:
        verbose_name_plural = "User Profiles"
        verbose_name = "User Profile"
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name ='user_profile', verbose_name = "User")
    bio = models.CharField(max_length=1024, verbose_name = "User bio")
    urls = models.ManyToManyField(SocialURL, blank=True, related_name ='user_urls', verbose_name = "User Urls")
    imageurl = models.URLField(max_length=1024,blank=True, default=None, null=True, verbose_name="Profile picture")
    image = models.ImageField(upload_to='profile/%Y/%m/%d', verbose_name = "profile image",default=None, null=True,)
    
    def __str__(self):
        if self.user.get_full_name() == " ":
            return self.user.username
        else:
            return self.user.get_full_name()

class SiteSetting(IndexedTimeStampedModel):
    class Meta:
        verbose_name_plural = "Site settings"
        verbose_name = "Site settings"
    defprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE ,related_name ='user_profile', verbose_name = "Default Profile")
    maxblog = models.IntegerField(verbose_name = "Max Blog on home")
    sitetitle = models.CharField(max_length=150,unique=True, verbose_name = "Site title")
    disqusname = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Disqus short name")
    googleanalyticid = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Google analytics ID")
    keywords = models.CharField(max_length=512,blank=True, default=None, null=True, verbose_name = "Site SEO keywords")
    sitevarification = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Google Site Verification")
    description = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Site Description")
    twitterid =  models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Twitter Handle")
    fbappid = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Twitter Handle")
    fblink = models.URLField(max_length=1024,blank=True, default=None, null=True, verbose_name="Facebook Page link")
    locale = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Site Locale")
    icon = models.ImageField(upload_to='icon/%Y/%m/%d', verbose_name = "Site Favicon",default=None, null=True,blank=True)
    iconurl = models.URLField(max_length=1024,blank=True, verbose_name = "Favicon url",default=None, null=True)
    site_name = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "FB site name")
    def __str__(self):
        return self.defprofile.__str__()
