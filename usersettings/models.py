from django.db import models
from django.contrib.auth.models import User

from posts.models import IndexedTimeStampedModel, SluggedModel, get_uniqueslug

from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

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
    # imageurl = models.URLField(max_length=1024,blank=True, default=None, null=True, verbose_name="Profile picture")
    # image = models.ImageField(upload_to='profile/%Y/%m/%d',blank=True, default=None, null=True, verbose_name = "profile image")
    image =CloudinaryField(verbose_name = 'Profile picture',blank=True, default=None, null=True)
    def __str__(self):
        if self.user.get_full_name() == " " or self.user.get_full_name() == "":
            return self.user.username
        else:
            return self.user.get_full_name()



class Projects(SluggedModel):
    class Meta:
        verbose_name_plural = "Projects"
        verbose_name = "Project"
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name ='user_project', verbose_name = "User")
    title = models.CharField(max_length=150, unique=True, verbose_name = "Project title")
    summary = models.CharField(max_length=125, blank=True, default=None, null=True,verbose_name = "Project summary")
    details = models.TextField(verbose_name = "Project details", blank=True, default=None, null=True)
    thumbnail = CloudinaryField(verbose_name = 'Thumbnail',blank=True, default=None, null=True)
    image = CloudinaryField(verbose_name = 'Featured image',blank=True, default=None, null=True)
    # thumburl = models.URLField(max_length=1024, verbose_name = "Thumbnail url",blank=True,default=None, null=True)
    # thumbnail = models.ImageField(upload_to='project/%Y/%m/%d', verbose_name = "Project Thumbnail",default=None, null=True,blank=True)
    # blogurl = models.URLField(max_length=1024,blank=True, default=None, null=True, verbose_name="Blog URL")
    liveurl = models.URLField(max_length=1024, verbose_name = "Live url",blank=True,default=None, null=True)
    codeurl = models.URLField(max_length=1024, verbose_name = "Code url",blank=True,default=None, null=True)

    def get_absolute_url(self):
        return "/project/"+self.slug

    def save(self , *args, **kwargs):
        slug = get_uniqueslug(Projects,self.title)
        # if its new record
        if self.pk is None:
            self.slug = slug
        # if title got changed
        if slugify(self.title) not in self.slug and (not slugify(self.title) == ""):
            self.slug = slug

        super(Projects, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

class SiteSetting(IndexedTimeStampedModel):
    class Meta:
        verbose_name_plural = "Site settings"
        verbose_name = "Site settings"
    defprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE ,related_name ='user_main', verbose_name = "Default Profile")
    maxblog = models.IntegerField(verbose_name = "Max Blog on home")
    siteurl = models.URLField(max_length=1024, verbose_name = "Website url",blank=True,default=None, null=True)
    sitetitle = models.CharField(max_length=150,unique=True, verbose_name = "Site title")
    contact_msg = models.CharField(max_length=512, blank=True, default=None, null=True,  verbose_name = "Contact Message")
    disqusname = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Disqus short name")
    googleanalyticid = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Google analytics ID")
    keywords = models.CharField(max_length=512,blank=True, default=None, null=True, verbose_name = "Site SEO keywords")
    sitevarification = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Google Site Verification")
    description = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Site Description")
    twitterid =  models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Twitter Handle")
    fbappid = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Twitter Handle")
    fblink = models.URLField(max_length=1024,blank=True, default=None, null=True, verbose_name="Facebook Page link")
    locale = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "Site Locale")
    icon = CloudinaryField(verbose_name = 'Favicon',blank=True, default=None, null=True)
    # icon = models.ImageField(upload_to='icon/%Y/%m/%d', verbose_name = "Site Favicon",default=None, null=True,blank=True)
    # iconurl = models.URLField(max_length=1024,blank=True, verbose_name = "Favicon url",default=None, null=True)
    site_name = models.CharField(max_length=150,blank=True, default=None, null=True, verbose_name = "FB site name")
    def __str__(self):
        return self.defprofile.__str__()
