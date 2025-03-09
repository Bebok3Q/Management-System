from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def hello(request):
    template = loader.get_template("hello.html")
    return HttpResponse(template.render(request=request))