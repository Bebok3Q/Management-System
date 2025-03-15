from django.db import models
from django.core.mail import send_mail
from django.utils.timezone import now

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    supplier = models.CharField(max_length=255)

    # def __str__(self):
    #     return f"{self.name}"

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField()
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

class Inventory(models.Model):
    warehouse = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    stock_level = models.IntegerField(default=0)
    low_stock_threshold = models.PositiveBigIntegerField(default = 10)
    
    def is_low_stock(self):
        return self.stock_level <= self.low_stock_threshold
    
    def update_stock(self, quantity_change):
        self.stock_level += quantity_change
        self.save()

        if self.is_low_stock():
            self.send_low_stock_alert()

    def send_low_stock_alert(self):
        subject=f"Low Stock Alert: {self.product.name}"
        message = f"The stock for {self.product.name} is low ({self.stock_level} remaining)."
        send_mail(subject,message,'k.talaga3@gmail.com', ['k.talaga3@gmail.com'])

class StockTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('restock', 'Restock'),
        ('sale', 'Sale'),
        ('adjustment', 'Manual Adjustment'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.quantity} units of {self.product.name}"