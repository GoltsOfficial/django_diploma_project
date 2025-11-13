from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
path('frontend/frontend/static', RedirectView.as_view(url='/')),
    # Рут шаблон:
    path('', include('frontend.urls')),
    # Панель админа
    path('admin/', admin.site.urls),
    # Остальные пути
    path('api/auth/', include('apps.auth_app.urls')),
    path('api/catalog/', include('apps.catalog.urls')),
    path('api/basket/', include('apps.basket.urls')),
    path('api/orders/', include('apps.order.urls')),
    path('api/payment/', include('apps.payment.urls')),
    path('api/userprofile/', include('apps.userprofile.urls')),
    path('api/tags/', include('apps.tags.urls')),
    path('api/product/', include('apps.product.urls')),
]
