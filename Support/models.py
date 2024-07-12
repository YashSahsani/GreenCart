# Support/models.py

from django.db import models
from django.conf import settings

class Query(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    query_type_choices = [
        ('order_status', 'Order Status'),
        ('order_delivery', 'Order Delivery'),
        ('other', 'Other'),
    ]
    type = models.CharField(max_length=20, choices=query_type_choices)
    description = models.TextField()
    attachment = models.FileField(upload_to='query_attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.type}"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


