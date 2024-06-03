from django.contrib import admin
from django.urls import path, include
from guestbook_app import views

urlpatterns = [
    path('register/',views.signup,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('',views.guestbook,name='guestbook'),
]