from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField(default=0)
    enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
