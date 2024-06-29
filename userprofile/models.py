from django.db import models
from Auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default='1990-01-01', blank=True, null=True)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(max_length=255, blank=True,default='-')
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')

    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    # Create a profile for new users automatically
    def create_profile(sender, **kwargs):
        if kwargs['created']:
            UserProfile.objects.create(user=kwargs['instance'])

    models.signals.post_save.connect(create_profile, sender=User)
