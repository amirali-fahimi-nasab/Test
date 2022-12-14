from django.urls import path

from . import views as products_views

urlpatterns = [
  path('list_products/',products_views.list_views_product , name = 'list_products'),
  path('<int:product_id>/show_object/' , products_views.show_object , name = 'show_object'),
  path('create_product/' , products_views.create_view_product , name = 'create_product'),
  path('<int:product_id>/update_product/',products_views.update_view_product , name ='update_product'),
  path('<int:product_id>/delete_product/' , products_views.delete_view_product , name ='delete_product'),
  path('<int:product_id>/change_price/',products_views.ChangePriceProduct.as_view() , name ='change_price'),
  ]

