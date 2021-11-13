from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    image = models.ImageField()
    price = models.FloatField()
    category = models.Model(Category)
