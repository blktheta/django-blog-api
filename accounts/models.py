from django.db import models
# Extend Custom user model from AbstractUser
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
