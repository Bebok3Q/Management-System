from django.db import models

# Create your models here.

class Product(models.Model):
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
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

class Inventory(models.Model):
    warehouse = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    stock_level = models.IntegerField()