from django.conf.urls import url

from django.urls import path,include
from django.conf import settings
from .views import home_view, blog_view, about_view, subscribe_view, unsubscribe_view,  project_view, single_project_view
from .feed import PostsFeed
from .views import share_view
urlpatterns = [
    url(r"^$", home_view, name ="home_page"),
    path('about/', about_view, name ="about_view"),
    path('project/', project_view, name ="project_view"),
    path('blog/', home_view, name ="home_page"),
    path('subscribe/', subscribe_view, name ="subscribe_page"),
    path('subscription/<str:slug>', unsubscribe_view, name ="subscribe_page"),
    path('subscription/', unsubscribe_view, name ="subscribe_page"),
    path('blog/<str:slug>/', blog_view, name ="blog_page"),
    path('project/<str:slug>/', single_project_view, name ="single_project_view"),
    path('feed/', PostsFeed()),
    path('share/', share_view),
    # path('/', home_view, name ="home_page"),
]
