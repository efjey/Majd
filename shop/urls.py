
from .views import helloAdmin, about
from django.urls import path, include
 

urlpatterns = [
  
    path('', helloAdmin, name="home"),
    path('about/', about, name="about"),
    
]
