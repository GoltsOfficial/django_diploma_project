from django.urls import path
from . import views

urlpatterns = [
    path('', views.tags_list, name='tags'),
    path('<int:id>/', views.tag_products, name='tag_products'),
]
