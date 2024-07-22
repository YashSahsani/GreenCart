from django.db import models

from Shop.models import Product


# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user_id = models.CharField(max_length=10,default="1")

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.quantity * self.product.discount_price


class WishlistItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=10,default="1")

    def __str__(self):
        return self.product.name
