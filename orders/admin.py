from django.contrib import admin
from .models.order import Order
from .models.order_line import Order_Line

# Register your models here.
admin.site.register(Order)
admin.site.register(Order_Line)
