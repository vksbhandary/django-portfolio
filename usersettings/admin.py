from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import UserProfile, UserURL, ProfileEntries, UserSkill, SiteSetting

class SocialURLAdmin(admin.ModelAdmin):
    list_display = ('type', 'link')

admin.site.register(SocialURL,SocialURLAdmin)

class UserProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio',)
    list_display = ('title', 'user')

admin.site.register(UserProfile, UserProfileAdmin)


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ( 'defprofile', 'maxblog', 'sitetitle')

admin.site.register(SiteSetting, SiteSettingAdmin)