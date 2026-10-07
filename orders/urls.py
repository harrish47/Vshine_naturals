from django.urls import path
from . import views

app_name = 'order'

urlpatterns=[
    path("My_orders/", views.my_orders, name='my_orders'),
    path("place_order/", views.place_order, name='place_order'),
]