
from . import views
from django.urls import path
 

urlpatterns = [
  
    path('', views.helloAdmin, name="home"),
    path('about/', views.about, name="about"),
    path('learn/', views.learn, name="learn"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup_user, name="signup"),
    path('product/<int:pk>', views.product, name="product"),
    path('category/<str:cat>', views.category, name="category"),
    path('category/', views.category_summary, name="category_summary"),

]
