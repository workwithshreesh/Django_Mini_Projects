from django.urls import path
from DailyQuotes_Django_projectApp import views

urlpatterns = [
    path('',views.index,name=''),
    path('about/',views.about,name='about-us'),
    path('contact/',views.contact,name='contact-us')
]