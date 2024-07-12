from django.db import models

# Create your models here.
class navCategories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class offer(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='offers_poster/')

    def __str__(self):
        return self.title