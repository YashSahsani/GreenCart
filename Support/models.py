# Support/models.py

from django.db import models
from django.conf import settings
import random
class Query(models.Model):
    query_type_choices = [
        ('order_status', 'Order Status'),
        ('order_delivery', 'Order Delivery'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    type = models.CharField(max_length=20, choices=query_type_choices)
    description = models.TextField()
    attachment = models.FileField(upload_to='query_attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ticket_number = models.IntegerField(unique=True, editable=False, null = True)

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = random.randint(10000, 99999)
        super().save(*args, **kwargs)
        if not self.statuses.exists(): # else ticketstatus_set
            TicketStatus.objects.create(query=self, status='open')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.type}"
class TicketStatus(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='statuses')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.query.ticket_number} - {self.status} at {self.updated_at}"

class faqCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.ForeignKey(faqCategory, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.question

