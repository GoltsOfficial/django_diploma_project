from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket_view, name='basket'),
    path('add/', views.add_to_basket, name='add_to_basket'),
    path('remove/<int:id>/', views.remove_from_basket, name='remove_from_basket'),
    path('update/<int:id>/', views.update_basket, name='update_basket'),
]
