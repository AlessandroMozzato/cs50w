from django.db import models

# Create your models here.
class Menu(models.Model):
    class_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    num_toppings = models.CharField(max_length=30)
    size = models.BooleanField(default=True)
    price = models.IntegerField()
    price_big = models.IntegerField(null=True)