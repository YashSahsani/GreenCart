from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry = models.IntegerField(default=3)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='products/')
    in_stock = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.CharField(max_length=10,default="1")
    expiry_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def expire_date(self):
        return self.created_at + timedelta(days=self.expiry)

    def days_left(self):
        now = timezone.now()
        expire_date = self.expire_date()
        delta = expire_date - now
        return delta.days


class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    def __str__(self):
        return self.name

@receiver(post_save, sender=Product)
def set_expiry_date(sender, instance, created, **kwargs):
    if created:  # Only calculate expiry_date if a new instance is created
        instance.expiry_date = instance.created_at + timedelta(days=instance.expiry)
        instance.save()