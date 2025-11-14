from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('profile/password', views.profile_password, name='profile_password'),
    path('profile/avatar', views.profile_avatar, name='profile_avatar'),
]