from django.shortcuts import render

from .models import Post
from django.core.paginator import Paginator

from usersettings.models import SiteSetting, UserProfile
# Create your views here.

def home_view(request):
	blogs = Post.objects.filter(status='published').order_by('-published')
	paginator = Paginator(blogs,1)
	page = int(request.GET.get('page',1))
	blog_obj = paginator.get_page(page)
	template = 'home.html'
	context = {'posts':blog_obj.object_list, 'page':page, 'last_page': paginator.num_pages }
	
	if page < paginator.num_pages:
		context['next_page'] = page+1

	if page > 1:
		context['prev_page'] = page-1
	
		

	return render(request, template,context)


def blog_view(request, slug):
	blog = Post.objects.filter(slug=slug).first()
	setting = SiteSetting.objects.all().first()
	creator = UserProfile.objects.filter(user=blog.author).first()
	template = 'blog.html'
	context = {'post':blog }

	if creator:
		context['author_image_url'] = creator.imageurl
		context['author_image'] = creator.image
		
	if setting:
		context['page_id'] = blog.slug
		context['page_url'] = setting.siteurl + blog.get_absolute_url()
		context['setting'] = setting
		

		
	return render(request, template,context)
	