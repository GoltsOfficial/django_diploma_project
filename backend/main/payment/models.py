from django.db import models


class Payment(models.Model):
    # Строковая ссылка
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, related_name='payments')
    number = models.CharField(max_length=16)
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    code = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for order #{self.order.id}"