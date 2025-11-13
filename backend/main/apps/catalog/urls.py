from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_list, name='catalog'),
    path('<int:id>/', views.catalog_detail, name='catalog_detail'),
    path('categories/', views.categories, name='categories'),
    path('sale/', views.sale_products, name='sale'),
]
