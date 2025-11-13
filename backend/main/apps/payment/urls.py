from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.payment, name='payment'),
    path('someone/', views.payment_someone, name='payment_someone'),
    path('progress/', views.payment_progress, name='payment_progress'),
]
