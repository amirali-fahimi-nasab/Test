from django.urls import path

from . import views as accounts_views

urlpatterns = [
  path('login/' , accounts_views.LoginView.as_view() , name='login'),
  path('list_users/' , accounts_views.ListUsersViews.as_view() , name = 'list_users'),
  path('register/' , accounts_views.Register.as_view() , name = 'register'),

  ]