from django.shortcuts import render

from .models import Post
from django.core.paginator import Paginator

from usersettings.models import SiteSetting, UserProfile
# Create your views here.
from django.shortcuts import get_object_or_404

def handler404(request, exception):
	template = '404.html'
	context= {}
	return render(request, template,context)


def home_view(request):
	blogs = Post.objects.filter(status='published').order_by('-published')
	setting = SiteSetting.objects.all().first()
	max_pages = 10
	if setting and setting.maxblog > 0:
		max_pages = setting.maxblog

	paginator = Paginator(blogs,max_pages)
	page = int(request.GET.get('page',1))
	blog_obj = paginator.get_page(page)
	template = 'home.html'
	context = {'posts':blog_obj.object_list, 'page':page, 'last_page': paginator.num_pages }
	
	if page < paginator.num_pages:
		context['next_page'] = page+1

	if page > 1:
		context['prev_page'] = page-1

	if setting:
		context['setting']= setting
		context['sociallinks'] = setting.defprofile.urls.all()

	return render(request, template,context)


def blog_view(request, slug):
	blog = get_object_or_404(Post, slug=slug)
	setting = SiteSetting.objects.all().first()
	creator = UserProfile.objects.filter(user=blog.author).first()
	template = 'blog.html'
	context = {'post':blog }

	if creator:
		context['author_image_url'] = creator.imageurl
		context['author_image'] = creator.image

	if setting:
		context['page_id'] = blog.slug
		context['setting'] = setting
		context['sociallinks'] = setting.defprofile.urls.all()
		
		if setting.siteurl:
			context['page_url'] = setting.siteurl + blog.get_absolute_url()
		else:
			context['page_url'] = request.get_host() + blog.get_absolute_url()
		
	return render(request, template,context)


def about_view(request):
	setting = SiteSetting.objects.all().first()
	template = 'about-me.html'
	context = {}
	if setting:
		context['setting'] = setting
		context['sociallinks'] = setting.defprofile.urls.all()
		
	return render(request, template,context)

	