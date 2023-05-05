from category.models import Category
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(max_length=100, upload_to='products/images', blank=True)
    description = models.TextField(max_length=2048, blank=True, default='')
