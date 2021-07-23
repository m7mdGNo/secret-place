from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.static import serve
import django.conf.global_settings as settings

urlpatterns = [

    path('',views.home,name='home'),
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('profile/setting/',views.setting,name='setting'),
    path('profile/<str:pk>/',views.Profile_User,name='profile'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('search/',views.search,name='search'),


]

