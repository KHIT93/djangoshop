from django.db import models
from django.conf import settings
from .cart_item import CartItem
from products.models.product import Product

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    items = models.ManyToManyField(Product, through=CartItem)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)

    def update_total(self):
        print("updating cart totals...")
        subtotal = 0
        items = self.items.all()
        for item in items:
            subtotal += item.line_item_total
        self.total = "%.2f" %(subtotal)
        self.save()
