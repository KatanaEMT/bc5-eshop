from django.db import models
from django.contrib.auth.models import User
from costumerapp.models import Costumer


class NewsCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField(max_length=100)
    article = models.TextField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey(
        to=NewsCategory,
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    costumer_views = models.ManyToManyField(
        to=Costumer,
    )
    views_qty = models.IntegerField(default=0)

    def __str__(self):
        return self.title

