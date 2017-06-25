from django.db import models

class product():
    category_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    inventory = models.CharField(max_length=255)
    enabled = models.CharField(max_length=255)
