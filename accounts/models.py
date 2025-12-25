from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=50, choices=[
        ('citizen', 'Citizen'),
        ('admin', 'Admin'),
        ('officer', 'Officer'),
    ])
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'email']
    
    def __str__(self):
        return self.phone

