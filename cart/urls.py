from django.urls import path
from . import views

app_name = 'cart' 
urlpatterns=[
    path('cart/', views.view_cart, name= 'cart'),
    path('cart/add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>', views.remove_cart, name='remove_cart')
]