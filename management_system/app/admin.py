from django.contrib import admin
from .models import Product, Supplier, Order, Inventory
# Register your models here.

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'stock_level', 'low_stock_threshold', 'is_low_stock_status')

    def is_low_stock_status(self, obj):
        return obj.is_low_stock()
    is_low_stock_status.boolean = True
    is_low_stock_status.short_description = 'Low Stock'



class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "stock", "price")

admin.site.register(Product, MemberAdmin)
admin.site.register(Supplier)
admin.site.register(Order)
# admin.site.register(Inventory)
