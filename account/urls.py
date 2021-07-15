from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('profile/setting/',views.setting,name='setting'),
    path('profile/<str:pk>/',views.Profile_User,name='profile'),


]
