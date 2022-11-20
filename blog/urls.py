from django.urls import path

from . import views as blog_views

urlpatterns = [
   path('list_blogs/' , blog_views.list_views_blogs , name ='list_blogs'),
   ]
