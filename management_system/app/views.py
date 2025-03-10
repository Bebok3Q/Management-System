from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.http import HttpResponse
from django.template import loader
from .models import Product
from django_tables2 import SingleTableView
from .tables import ProductTable
from django.views.generic import ListView
from .forms import ProductForm
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