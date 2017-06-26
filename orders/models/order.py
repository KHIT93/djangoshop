from django.db import models
from django.contrib.auth.models import User
from customers.models.customer import Customer

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    invoiced = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.customer)

    def update_total(self):
        print("updating order totals...")
        subtotal = 0
        for item in self.orderline_set.all():
            subtotal += item.line_item_total
        self.total = "%.2f" %(subtotal)
        self.save()
