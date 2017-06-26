from django.db import models
from .order import Order
from products.models.product import Product
from django.db.models.signals import pre_save, post_save, post_delete

class OrderLine(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=0)
    line_item_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.order)

def order_line_pre_save_receiver(sender, instance, *args, **kwargs):
    qty = int(instance.quantity)
    if qty >= 1:
        price = instance.product.price
        line_item_total = Decimal(qty) * Decimal(price)
        instance.line_item_total = line_item_total

def order_line_post_save_receiver(sender, instance, *args, **kwargs):
    instance.cart.update_total()

pre_save.connect(order_line_pre_save_receiver, sender=OrderLine)

post_save.connect(order_line_post_save_receiver, sender=OrderLine)

post_delete.connect(order_line_post_save_receiver, sender=OrderLine)
