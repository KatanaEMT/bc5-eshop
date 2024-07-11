from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    bio = models.TextField()
    social_link = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    user = models.OneToOneField(
        to=User,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )


class Costumer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    user = models.OneToOneField(
        to=User,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    def __str__(self):
        return self.name
