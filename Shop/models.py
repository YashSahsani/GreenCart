from django.db import models
import django.utils.timezone
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry = models.IntegerField(default=3)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='products/')
    in_stock = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.CharField(max_length=10,default="1")

    def __str__(self):
        return self.name

class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    def __str__(self):
        return self.name
