from django.shortcuts import render

from .models import Post
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
	blogs = Post.objects.filter(status='published').order_by('-published')
	paginator = Paginator(blogs,1)
	page = int(request.GET.get('page',1))
	blog_obj = paginator.get_page(page)
	template = 'home.html'
	if page < paginator.num_pages:
		context = {'posts':blog_obj.object_list, 'page':page, 'next_page':page+1, 'last_page': paginator.num_pages }
	else:
		context = {'posts':blog_obj.object_list, 'page':page, 'last_page': paginator.num_pages }
		
	return render(request, template,context)


def blog_view(request, slug):
	blog = Post.objects.filter(slug=slug).first()
	template = 'blog.html'
	context = {'post':blog }
	return render(request, template,context)
	