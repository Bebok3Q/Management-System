from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.http import HttpResponse
from django.template import loader
from .models import Product, Order, Inventory, StockTransaction
from django_tables2 import SingleTableView
from .tables import ProductTable, OrderTable
from django.views.generic import ListView
from .forms import ProductForm, OrderForm, StockTransactionForm
from django.contrib import messages
from django.db.models import F
from .serializers import ProductSerializer, StockTransactionSerializer
from rest_framework import viewsets

# Create your views here.

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render(request=request))


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

class ProductListView(SingleTableView):
    model = Product
    table_class = ProductTable
    template_name = 'products/product_list.html'

def product_create(request):
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm
    return render(request, 'products/product_form.html', {'form': form})


def product_update(request ,id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form':form})

def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method =="POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_delete.html', {'product': product})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

class OrderListView(SingleTableView):
    model = Order
    table_class = OrderTable
    template_name = 'orders/order_list.html'

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_list")
    else:
        form = OrderForm()
    return render(request, 'orders/order_list.html', {'form': form}) 

def order_edit(request, id):
    order = get_object_or_404(Order, pk=id)
    if request.method=="POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form':form})

def order_delete(request, id):
    order = get_object_or_404(Order, pk=id)
    if request.method == "POST":
        order.delete()
        return redirect("order_list")
    return render(request, 'orders/order_delete.html', {'order': order})

def update_stock(request, product_id, quantity):
    product = get_object_or_404(Product, id=product_id)
    inventory = get_object_or_404(Inventory, product=product)

    inventory.update_stock(quantity)
    messages.success(request, f"Stock updated! New stock level: {inventory.stock_level}")

    return redirect('product_list')


def adjust_stock(request):
    if request.method == "POST":
        form = StockTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()

            # Update the product's stock level
            if transaction.transaction_type == "restock":
                transaction.product.stock_level += transaction.quantity
            elif transaction.transaction_type in ["sale", "adjustment"]:
                transaction.product.stock_level -= transaction.quantity

            transaction.product.save()
            return redirect("dashboard")

    else:
        form = StockTransactionForm()

    return render(request, "adjust_stock.html", {"form": form})



def dashboard(request):
    low_stock_items = Inventory.objects.filter(stock_level__lte=F('low_stock_threshold'))
    return render(request, 'dashboards/dashboard.html', {'low_stock_items': low_stock_items})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StockTransactionViewSet(viewsets.ModelViewSet):
    queryset = StockTransaction.objects.all()
    serializer_class = StockTransactionSerializer