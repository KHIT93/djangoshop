from django.db import models
from products.models.product import Product

class CartItem(models.Model):
	cart = models.ForeignKey("Cart")
	product = models.ForeignKey(Product)
	quantity = models.PositiveIntegerField(default=1)
	line_item_total = models.DecimalField(max_digits=10, decimal_places=2)
