from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=2048)
    description = models.CharField(max_length=2048, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=2048)
