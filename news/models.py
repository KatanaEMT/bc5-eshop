from django.db import models
from django.contrib.auth.models import User


class New(models.Model):
    title = models.CharField(max_length=50)
    article = models.TextField()
    views = models.IntegerField(default=0)
    user_views = models.ManyToManyField(
        to=User,
        blank=True,
    )
    
    def __str__(self):
        return self.title

