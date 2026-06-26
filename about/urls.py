from django.urls import path
from .views import about_details

app_name = 'about' 
urlpatterns=[
    path('about/', about_details, name= 'about')
]