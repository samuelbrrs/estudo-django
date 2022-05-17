from django.contrib.auth.models import AbstractUser
from django.db import models

class User (AbstractUser):
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)

# Create your models here.
