from django.contrib import admin
from .models.order import Order
from .models.order_line import Order_Line

class Order_LineAdmin(admin.ModelAdmin):
    list_display = ["__str__", "product", "quantity", "created_at"]
    class Meta:
        model = Order_Line

# Register your models here.
admin.site.register(Order)
admin.site.register(Order_Line, Order_LineAdmin)
