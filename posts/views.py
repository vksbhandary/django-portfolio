from django.shortcuts import render

from .models import Post, Subscriber
from django.core.paginator import Paginator

from usersettings.models import SiteSetting, UserProfile, Projects
# Create your views here.
from django.shortcuts import get_object_or_404
from django.core.validators import validate_email
from .forms import SubscribeForm, UnsubscribeForm

from django.forms import ValidationError


def handler404(request, exception):
	template = '404.html'
	context= {}
	return render(request, template,context)

def handle_list_view(request, posts, is_search=False):
	setting = SiteSetting.objects.all().first()
	max_pages = 10
	if setting and setting.maxblog > 0:
		max_pages = setting.maxblog

	paginator = Paginator(posts,max_pages)
	page = int(request.GET.get('page',1))
	blog_obj = paginator.get_page(page)
	template = 'home.html'
	count = posts.count()

	context = {'posts':blog_obj.object_list, 'count':count , 'page':page, 'last_page': paginator.num_pages }
	
	if is_search:
		context['is_search'] = True
		context['query'] = request.GET.get('q',None) or request.POST.get('q',None)

	if page < paginator.num_pages:
		context['next_page'] = page+1

	if page > 1:
		context['prev_page'] = page-1

	if setting:
		context['setting']= setting
		context['sociallinks'] = setting.defprofile.urls.all()

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
	setting = SiteSetting.objects.all().first()
	creator = UserProfile.objects.filter(user=blog.author).first()
	template = 'blog.html'
	context = {'post':blog }

	if creator:
		context['author_image_url'] = creator.image #creator.imageurl
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



def project_view(request):
	template = 'projects.html'
	setting = SiteSetting.objects.all().first()
	context = {'projects':None, 'count':0}
	# print(setting)
	# print(setting.defprofile.user)
	if setting:
		print(setting.defprofile.user)
		projects = Projects.objects.filter(user=setting.defprofile.user)
		context = {'projects':projects, 'count':projects.count()}
		context['setting'] = setting
		context['sociallinks'] = setting.defprofile.urls.all()
	print(context['sociallinks'] )	
	return render(request, template,context)

def unsubscribe_view(request, slug=False):
	context = {}
	setting = SiteSetting.objects.all().first()
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

	
	if setting:
		context['setting'] = setting
		context['sociallinks'] = setting.defprofile.urls.all()
	


def subscribe_view(request):
	template = 'subscribe.html'
	setting = SiteSetting.objects.all().first()
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


	if setting:
		context['setting'] = setting
		context['sociallinks'] = setting.defprofile.urls.all()
		
	return render(request, template,context)

	