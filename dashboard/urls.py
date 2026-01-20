# dashboard/urls.py
from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name='dashboard'),        # agar homepage dashboard hai
    path('profile/', views.profile, name='profile'),    # yeh line zaruri hai!
]
