from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(max_length=100, unique=True)

  class Meta:
    ordering = ('-name',)

class Product(models.Model):
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)