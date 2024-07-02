# payments/models.py

from django.db import models

class Payment(models.Model):
    Name = models.CharField(max_length=255,default="John")
    Description = models.CharField(max_length=255)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.email} - {self.amount}"
