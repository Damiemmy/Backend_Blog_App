from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    state=models.CharField(max_length=100, blank=True,null=True)
    address=models.CharField(max_length=150,blank=True,null=True)
    phone=models.CharField(max_length=20,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
   
    def __str__(self):
        return self.username
