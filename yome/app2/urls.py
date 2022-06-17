from django.urls import path
from .views import  signup

#registering the yrl
urlpatterns = [
    path("signup/", signup ),
    
]
