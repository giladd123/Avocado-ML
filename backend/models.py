from django.db import models

# Create your models here.

class AvocadoInput(models.Model):
    total_volume = models.FloatField()
    type_4046 = models.IntegerField()
    type_4225 = models.IntegerField()
    type_4770 = models.IntegerField()

    total_bags = models.IntegerField()
    small_bags = models.IntegerField()
    large_bags = models.IntegerField()
    XL_bags = models.IntegerField()

    type = models.TextField()
    year = models.IntegerField()
    region = models.TextField()

class AvocadoOutput(models.Model):
    price = models.FloatField()