from django.urls import path

from . import views as accounts_views



urlpatterns = [
  path('logout/' , accounts_views.Logout.as_view() , name='logout'),
  path('list_users/' , accounts_views.list_users , name = 'list_users'),
  path('register/' , accounts_views.RegisterUser.as_view() , name = 'register'),
  path('create_superuser/' , accounts_views.CreateSuperUser.as_view() , name='create_superuser'),
  path('change_mobile/' , accounts_views.ChangeMobile.as_view() , name ='change_mobile'),
  path('<int:pk>/set_username/' , accounts_views.ChangeUsername.as_view() , name='change_username'),
  path('<int:user_id>/set_password/' , accounts_views.ChangePasswordView.as_view() , name ='set_password'),
  path('<int:pk>/delete_user/', accounts_views.DeleteUser.as_view() , name ='delete_user'),

  ]





