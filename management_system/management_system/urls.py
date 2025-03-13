"""
URL configuration for management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import ProductListView, product_create, product_update, home, product_delete, OrderListView, order_edit, order_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('list/', ProductListView.as_view(), name='product_list'),
    path('create/', product_create, name='product_create'),
    path('<int:id>/edit/', product_update, name='product_update'),
    path('<int:id>/delete/', product_delete, name='product_delete'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('order/<int:id>/edit/', order_edit, name='order_edit'),
    path('order/<int:id>/delete/', order_delete, name='order_delete')
]
