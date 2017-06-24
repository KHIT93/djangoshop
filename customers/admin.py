from django.contrib import admin

from .models.customer import Customer
from .models.stripe_customer import StripeCustomer
# Register your models here.

admin.site.register(Customer)
admin.site.register(StripeCustomer)
