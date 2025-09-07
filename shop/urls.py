
from .views import *
from django.urls import path, include
 

urlpatterns = [
  
    path('', helloAdmin, name="home"),
    path('about/', about, name="about"),
    path('learn/', learn, name="learn"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
]
