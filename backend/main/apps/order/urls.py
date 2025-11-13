from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='orders'),
    path('<int:id>/', views.order_detail, name='order_detail'),
    path('create/', views.create_order, name='create_order'),
    path('history/', views.order_history, name='order_history'),
]
