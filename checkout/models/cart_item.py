from decimal import Decimal
from django.db import models
from products.models.product import Product
from django.db.models.signals import pre_save, post_save, post_delete

class CartItem(models.Model):
	cart = models.ForeignKey("Cart")
	product = models.ForeignKey(Product)
	quantity = models.PositiveIntegerField(default=1)
	line_item_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)


def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
	qty = int(instance.quantity)
	if qty >= 1:
		price = instance.product.price
		line_item_total = Decimal(qty) * Decimal(price)
		instance.line_item_total = line_item_total

def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
	instance.cart.update_total()

pre_save.connect(cart_item_pre_save_receiver, sender=CartItem)

post_save.connect(cart_item_post_save_receiver, sender=CartItem)

post_delete.connect(cart_item_post_save_receiver, sender=CartItem)
