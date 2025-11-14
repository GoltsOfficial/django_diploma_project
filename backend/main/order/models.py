from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Принят'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
    ]

    DELIVERY_TYPES = [
        ('free', 'Бесплатная'),
        ('paid', 'Платная'),
        ('express', 'Экспресс'),
    ]

    PAYMENT_TYPES = [
        ('online', 'Онлайн'),
        ('offline', 'При получении'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    createdAt = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    deliveryType = models.CharField(max_length=20, choices=DELIVERY_TYPES, default='free')
    paymentType = models.CharField(max_length=20, choices=PAYMENT_TYPES, default='online')
    totalCost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='accepted')
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderProduct(models.Model):
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, related_name='products')
    # Строковая ссылка
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)