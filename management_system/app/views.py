from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.template import loader
from .models import Product
from django_tables2 import SingleTableView
from .tables import ProductTable
from django.views.generic import ListView
# Create your views here.

def hello(request):
    template = loader.get_template("hello.html")
    return HttpResponse(template.render(request=request))


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

class ProductListView(SingleTableView):
    model = Product
    table_class = ProductTable
    template_name = 'products/product_list.html'