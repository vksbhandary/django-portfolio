from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import UserProfile, SocialURL, SiteSetting
from .models import Projects

class SocialURLAdmin(admin.ModelAdmin):
    list_display = ('type', 'link')

admin.site.register(SocialURL,SocialURLAdmin)

class UserProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio',)
    list_display = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ( 'defprofile', 'maxblog', 'sitetitle')

admin.site.register(SiteSetting, SiteSettingAdmin)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'title')

admin.site.register(Projects, ProjectsAdmin)
