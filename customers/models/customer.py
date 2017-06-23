from django.db import models
from django.contrib.auth.models import User

class Customer(User):
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    address3 = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
