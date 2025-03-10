from django.contrib import admin
from .models import Product, Supplier, Order, Inventory
# Register your models here.



class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "stock", "price")

admin.site.register(Product, MemberAdmin)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Inventory)
