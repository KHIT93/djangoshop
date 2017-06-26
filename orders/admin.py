from django.contrib import admin
from .models.order import Order
from .models.order_line import OrderLine

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ["__str__", "product", "quantity", "created_at"]
    class Meta:
        model = OrderLine

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderLine, OrderLineAdmin)
