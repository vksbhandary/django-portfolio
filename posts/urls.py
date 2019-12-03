from django.conf.urls import url

from django.urls import path,include
from django.conf import settings
from .views import home_view

urlpatterns = [
    url(r"^$", home_view, name ="home_page"),
    # path('/', home_view, name ="home_page"),
]
