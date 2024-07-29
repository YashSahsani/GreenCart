from django.db import models



class offer(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='offers_poster/')

    def __str__(self):
        return self.title
    
    
class Email(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email