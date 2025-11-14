from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('product/<int:id>/review', views.product_review, name='product_review'),
]