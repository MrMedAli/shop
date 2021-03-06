from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('<slug:slug>', views.product_details, name='product_details'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),

]