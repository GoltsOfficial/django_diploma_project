from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    # Строковая ссылка на Product из catalog
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, related_name='product_reviews')
    author = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    rate = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author}"