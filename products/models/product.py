from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    description = models.TextField()
    inventory = models.IntegerField(default=0)
    enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
