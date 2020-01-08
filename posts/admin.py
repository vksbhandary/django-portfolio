from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Tag, Subscriber

class PostAdmin(SummernoteModelAdmin):
    exclude = ("slug",'author', 'published')
    summernote_fields = ('content',)
    list_display = ('title', 'slug','status','author','published')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)



class TagAdmin(admin.ModelAdmin):
    exclude = ("slug", 'count')
    list_display = ('title', 'slug', 'count')

admin.site.register(Tag, TagAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    exclude = ("code",)
    list_display = ('email', 'name', 'subscribed')

admin.site.register(Subscriber, SubscriberAdmin)
