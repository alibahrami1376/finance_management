from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    email = models.EmailField(unique=False, blank=True, null=True)

    objects = UserManager()

    def __str__(self):
        return self.username
