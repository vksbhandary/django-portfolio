from django.shortcuts import render

from .model import Post
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
	blogs = Post.objects.filter(status='published').order_by('-published')
	paginator = Paginator(blogs,1)
	page = int(request.GET.get('page',1))
	blog_obj = paginator.get_page(page)
    template = 'home.html'
    context = {'posts':blog_obj.object_list, 'page':page, 'last_page': paginator.num_pages }
    return render(request, template,context)