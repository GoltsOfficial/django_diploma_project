from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.title

    @property
    def image_data(self):
        if self.image:
            return {
                "src": self.image.url,
                "alt": self.title
            }
        return None


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    fullDescription = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=0)
    freeDelivery = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)
    reviews = models.PositiveIntegerField(default=0)
    limited = models.BooleanField(default=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt = models.CharField(max_length=200, blank=True)

    @property
    def src(self):
        return self.image.url


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    salePrice = models.DecimalField(max_digits=10, decimal_places=2)
    dateFrom = models.DateField()
    dateTo = models.DateField()


class Banner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)