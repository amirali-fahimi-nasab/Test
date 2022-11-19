from django.urls import path

from . import views as blog_views

urlpatterns = [
 path('list_blogs/', blog_views.ListViewsBlogs.as_view() , name='list_blogs'),
 path('create_blog/' , blog_views.CreateViewBlog.as_view() , name = 'create_blog'),
 path('<int:blog_id>/update_blog/' , blog_views.UpdateViewBlog.as_view() , name='update_blog'),
 ]