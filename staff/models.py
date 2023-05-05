from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Create your models here.
class Vehicle(models.Model):
    title = models.CharField(max_length=50)
    capacity = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}|{self.type}|{self.capacity}'


class Guide(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.lastName} {self.firstName}'


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
