from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, default='')
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    video_file = models.FileField(upload_to='video_files/', blank=True, null=True)
   

