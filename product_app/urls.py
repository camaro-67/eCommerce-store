from django.urls import path
from . import views

urlpatterns = [
    path('shop_list/',views.shop_list,name='shop_list'),
    path('blog/',views.blog),
path('create_cart/',views.create_item),
    path('shop_list/details/<slug:slug>',views.shop_details,name='shop_details'),
]