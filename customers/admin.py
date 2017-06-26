from django.contrib import admin

from .models.customer import Customer
from .models.stripe_customer import StripeCustomer
# Register your models here.

class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['address1', 'zip_code', 'state', 'country']
    class Meta:
        model = Customer

class StripeCustomerModelAdmin(admin.ModelAdmin):
    list_display = ['customer', 'stripe_id']
    class Meta:
        model = StripeCustomer

admin.site.register(Customer, CustomerModelAdmin)
admin.site.register(StripeCustomer, StripeCustomerModelAdmin)
