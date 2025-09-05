
from .views import helloAdmin
from django.urls import path, include
 

urlpatterns = [
  
    path('', helloAdmin),
    
]
