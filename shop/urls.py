
from . import views
from django.urls import path
 

urlpatterns = [
  
    path('', views.helloAdmin, name="home"),
    path('about/', views.about, name="about"),
    path('learn/', views.learn, name="learn"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup_user, name="signup"),
    path('update_user/', views.update_user, name="update_user"),
    path('update_password/', views.update_password, name="update_password"),
    path('update_info/', views.update_info, name="update_info"),
    path('product/<int:pk>', views.product, name="product"),
    path('category/<str:cat>', views.category, name="category"),
    path('category/', views.category_summary, name="category_summary"),
    path('search', views.search, name="search"),
    

]
