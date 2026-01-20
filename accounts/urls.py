# accounts/urls.py

from django.urls import path
from . import views

from django.shortcuts import render, redirect 


urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="create_account"),
    path('logout/', views.logout_request, name='logout')

]
