from django.contrib import admin

from .models.customer import Customer
from .models.stripe_customer import StripeCustomer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["__str__", "address1", "zip_code", "state" ,"country","created_at"]
    class Meta:
        model = Customer

class StripeCustomerAdmin(admin.ModelAdmin):
    list_display = ["__str__","created_at"]
    class Meta:
        model = StripeCustomer

admin.site.register(Customer, CustomerAdmin)
admin.site.register(StripeCustomer)
