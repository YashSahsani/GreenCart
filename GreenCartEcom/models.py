from django.db import models



class offer(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='offers_poster/')

    def __str__(self):
        return self.title