from django.urls import path

from . import views as blog_views



urlpatterns = [
   path('list_blogs/' , blog_views.BlogView.as_view({'get':'list'}) name = 'blog_views'),
   ]



