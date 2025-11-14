from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Фронтенд пути (из установленного пакета frontend)
    path('', include('frontend.urls')),

    # Редирект для кривой ссылки из фронтенда
    path('frontend/frontend/static', RedirectView.as_view(url='/')),

    # API пути - возвращают JSON
    path('api/sign-in', include('auth_app.urls')),
    path('api/sign-up', include('auth_app.urls')),
    path('api/sign-out', include('auth_app.urls')),
    path('api/categories', include('catalog.urls')),
    path('api/catalog', include('catalog.urls')),
    path('api/products/popular', include('catalog.urls')),
    path('api/products/limited', include('catalog.urls')),
    path('api/sales', include('catalog.urls')),
    path('api/banners', include('catalog.urls')),
    path('api/product/<int:id>', include('product.urls')),
    path('api/product/<int:id>/review', include('product.urls')),
    path('api/basket', include('basket.urls')),
    path('api/orders', include('order.urls')),
    path('api/orders/<int:id>', include('order.urls')),
    path('api/payment', include('payment.urls')),
    path('api/profile', include('userprofile.urls')),
    path('api/profile/password', include('userprofile.urls')),
    path('api/profile/avatar', include('userprofile.urls')),
    path('api/tags', include('tags.urls')),

    # Админка
    path('admin/', admin.site.urls),
]