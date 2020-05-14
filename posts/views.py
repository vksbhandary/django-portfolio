from django.shortcuts import render

from .models import Post, Subscriber
from django.core.paginator import Paginator

from usersettings.models import SiteSetting, UserProfile, Projects
# Create your views here.
from django.shortcuts import get_object_or_404
from django.core.validators import validate_email
from .forms import SubscribeForm, UnsubscribeForm
from .models import PostSettings

from django.forms import ValidationError
# import cloudinary
import cloudinary
from cloudinary import CloudinaryImage

from django.contrib.sites.shortcuts import get_current_site


def get_default_featured(context):
	post_def = PostSettings.objects.all().first()
	if post_def:
		context['default_thumb'] =  post_def.default_thumb
		context['default_featured'] = post_def.default_featured
	return context

def get_site_settings(request , context):
	setting = SiteSetting.objects.all().first()
	context['setting'] = None
	context['site_url'] = get_current_site(request).domain
	if setting:
		context['setting'] = setting
		context['sociallinks'] = setting.defprofile.urls.all()
		if setting.icon:
			context['favicon_url'] = str(setting.icon.url).replace("http://", "https://")
		if setting.siteurl:
			context['site_url'] = setting.siteurl
		
			
		
	return context

def handler404(request, exception):
	template = '404.html'
	context= {}
	return render(request, template,context)

def handle_list_view(request, posts, is_search=False):
	
	context = {}
	context =  get_site_settings(request, context)
	max_pages = 10
	setting = context['setting']
	if setting and setting.maxblog > 0:
		max_pages = setting.maxblog

	paginator = Paginator(posts,max_pages)
	page = int(request.GET.get('page',1))
	blog_obj = paginator.get_page(page)
	template = 'home.html'
	count = posts.count()

	# context = {'posts':blog_obj.object_list, 'count':count , 'page':page, 'last_page': paginator.num_pages }
	context['posts']  = blog_obj.object_list
	context['count']  = count
	context['page']  = page
	context['last_page']  = paginator.num_pages


	
	if is_search:
		context['is_search'] = True
		context['query'] = request.GET.get('q',None) or request.POST.get('q',None)

	if page < paginator.num_pages:
		context['next_page'] = page+1

	if page > 1:
		context['prev_page'] = page-1

	context = get_default_featured(context)
	# print(context)

	return render(request, template,context)


def blog_search(request):
	template = 'home.html'
	query = request.GET.get('q',None) or request.POST.get('q',None)
	blogs = Post.objects.filter(title__icontains=query, status='published').order_by('-published')
	
	return handle_list_view(request, blogs, is_search=True)

def home_view(request):
	if not request.GET.get('q',None) is None or not request.POST.get('q',None) is None :
		return blog_search(request)
	else:
		blogs = Post.objects.filter(status='published').order_by('-published')
		return handle_list_view(request, blogs)


def blog_view(request, slug):

	blog = get_object_or_404(Post, slug=slug)
	creator = UserProfile.objects.filter(user=blog.author).first()
	template = 'blog.html'

	context = {'post':blog}

	if creator and creator.image:
		context['author_image'] = creator.image

	context['page_id'] = blog.slug
	context =  get_site_settings(request, context)

	context['page_url'] = context['site_url']  + blog.get_absolute_url()
	context = get_default_featured(context)
	

	return render(request, template,context)



def single_project_view(request, slug):

	blog = get_object_or_404(Projects, slug=slug)
	creator = UserProfile.objects.filter(user=blog.user).first()
	template = 'project-details.html'

	context = {'post':blog}

	if creator and creator.image:
		context['author_image'] = creator.image

	context['page_id'] = blog.slug
	context =  get_site_settings(request, context)

	context['page_url'] = context['site_url']  + blog.get_absolute_url()
	context = get_default_featured(context)
	

	return render(request, template,context)



def about_view(request):
	template = 'about-me.html'
	context = {}
	context =  get_site_settings(request, context)
	return render(request, template,context)



def project_view(request):
	template = 'projects.html'
	context = {'projects':None, 'count':0}
	context =  get_site_settings(request, context)

	setting = context['setting']
	if setting:
		projects = Projects.objects.filter(user=setting.defprofile.user)
		context['projects'] = projects
		context['count'] = projects.count()
	return render(request, template,context)

# unsubscribe via update preference link on email (untested)
def unsubscribe_view(request, slug=False):
	context = {}

	if slug:
		sub = get_object_or_404(Subscriber, code=slug)
		form = Unsubscribe(initial=sub)
		template = 'subscribe.html'
	else:
		form = UnsubscribeForm(data=request.POST)
		if form.is_valid():
			sub = form.save()
			context['unsubscribe'] = True
			template = 'bye.html'

	context['subscriber'] = sub
	context =  get_site_settings(request, context)
	
	return render(request, template, context)


def subscribe_view(request):
	template = 'subscribe.html'
	email = request.POST.get('email',None)
	name = request.POST.get('name',None)
	context = {}
	context['form'] = SubscribeForm()
	context['new'] =  True
	if email:
		context['new'] = False
		try:
		    validate_email(email)
		except ValidationError as e:
			context['email_error'] = True
			
		else:
			# check if email already present
			sub = Subscriber.objects.filter(email=email).first()
			if sub:
				context['form'] = SubscribeForm(instance=sub)
				context['email_exists'] = True
				# context['form'] = SubscribeForm(instance=sub)
				if not name is None and not name == sub.name:
					sub.name = name
					sub.save()
			else:
				sub = Subscriber()
				sub.email = email
				sub.name = name
				sub.save()
				context['success'] = True
				template = 'bye.html'
				context['form'] = None

			context['subscriber'] = sub

		context =  get_site_settings(request, context)
		
	return render(request, template,context)

	