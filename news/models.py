from django.db import models


class New(models.Model):
    title = models.CharField(max_length=50)
    article = models.TextField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

