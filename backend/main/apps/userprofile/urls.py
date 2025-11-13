from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('update/', views.update_profile, name='update_profile'),
    path('account/', views.account_settings, name='account'),
    path('history/', views.order_history, name='order_history'),
]
