from category.models import Category
from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(max_length=100, upload_to='products/images', blank=True)
    description = models.TextField(max_length=2048, blank=True, default='')

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    def __str__(self):
        return self.name