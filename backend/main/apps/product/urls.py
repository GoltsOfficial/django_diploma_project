from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('search/', views.product_search, name='product_search'),
    path('popular/', views.popular_products, name='popular_products'),
]
