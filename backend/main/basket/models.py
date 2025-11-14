from django.db import models
from django.contrib.auth.models import User


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    # Строковая ссылка
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"