from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    phone = models.CharField(max_length=20, blank=True)
    user = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return f"{self.user.username} - Profile"
    