from django.db import models

# Create your models here.

class AvocadoInput(models.Model):

    small_bags = models.FloatField()
    large_bags = models.FloatField()
    XL_bags = models.FloatField()

    type = models.TextField()
    year = models.IntegerField()
    region = models.TextField()

class AvocadoOutput(models.Model):
    price = models.FloatField()