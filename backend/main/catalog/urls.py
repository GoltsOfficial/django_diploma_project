from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.categories, name='categories'),
    path('catalog', views.catalog, name='catalog'),
    path('products/popular', views.popular_products, name='popular_products'),
    path('products/limited', views.limited_products, name='limited_products'),
    path('sales', views.sales, name='sales'),
    path('banners', views.banners, name='banners'),
]