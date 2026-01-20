from django.db import models

# Create your models here.


class DareExchange(models.Model):
    name = models.CharField(max_length=100,null=False,blank=True)
    email = models.CharField(max_length=100) 
    phone_number = models.CharField(max_length=15)
    deadline = models.DateField(blank=True,null=True)

    # dare_image = models.FileField

    is_edited = models.BooleanField(default=False)
    dare = models.TextField()

    
