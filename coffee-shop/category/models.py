from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(max_length=100, upload_to='categories/images', blank=True)
    description = models.CharField(max_length=2048, blank=True)

    def __str__(self):
        return self.name