from django.db import models


# Create your models here.
class Client(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    passport_info = models.TextField()

    def __str__(self):
        return f'{self.lastName} {self.firstName}'
