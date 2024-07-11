from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Описание", null=True, blank=False)    
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    qty = models.IntegerField(default=0)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Категория",
    )
    
    def __str__(self):
        return self.name
        
