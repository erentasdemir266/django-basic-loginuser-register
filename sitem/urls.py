from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('base',views.base,name='base'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
    path('logoutpage',views.logoutpage,name='logoutpage'),


]