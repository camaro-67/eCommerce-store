from django.urls import path
from . import views

urlpatterns = [
    path('update_cart/<int:id2>',views.override_quantity, name='update_quantity'),
    path('find_cart/', views.find_cart),
    path('cart/add/<int:id1>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/',views.cart_detail,name='cart_detail'),
    path('find_price/',views.find_price),
    path('cart/remove/<int:removed_id>/',views.cart_remove,name='cart_remove'),
    path('cart/shopping_cart/',views.shopping_cart,name='shopping_cart'),
    path('cart/shopping_cart/checkout/',views.checkout,name='checkout'),
]