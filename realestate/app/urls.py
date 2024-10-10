from django.contrib import admin
from django.urls import path
from .views import register,logins,Home

urlpatterns = [
    path('home/',Home,name='Home'),
    path('login/',logins,name='logins'),
    path('signup/',register),

]