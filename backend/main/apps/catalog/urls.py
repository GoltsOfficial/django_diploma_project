from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('', views.CatalogView.as_view()),
    path('products/popular', views.PopularView.as_view()),
    path('products/limited', views.LimitedView.as_view()),
    path('sales', views.SalesView.as_view()),
    path('banners', views.BannersView.as_view()),
]
