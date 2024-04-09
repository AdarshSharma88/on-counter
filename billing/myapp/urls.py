# Import necessary modules
from django.contrib import admin
from django.urls import path
from django.db import models
from .models import Bill
from myapp.views import (
    generate_token, 
    employee_list, employee_detail,
    product_list, product_detail,
    customer_list, customer_detail,
    bill_list,
    top_selling_employee, top_selling_product,
    bill_item_list, bill_item_detail
)

# Define urlpatterns for routing
urlpatterns = [
    # Authentication API
    path('api/token/', generate_token, name='generate_token'),
    
    # Employee APIs
    path('api/employees/', employee_list, name='employee_list'),
    path('api/employees/<int:employee_id>/', employee_detail, name='employee_detail'),
    
    # Product APIs
    path('api/products/', product_list, name='product_list'),
    path('api/products/<int:product_id>/', product_detail, name='product_detail'),
    
    # Customer APIs
    path('api/customers/', customer_list, name='customer_list'),
    path('api/customers/<int:customer_id>/', customer_detail, name='customer_detail'),
    
    
    # Bill Item APIs
    path('api/bill_items/', bill_item_list, name='bill_item_list'),
    path('api/bill_items/<int:bill_item_id>/', bill_item_detail, name='bill_item_detail'),
    
    # Analytics APIs
    path('api/analytics/top-employee/', top_selling_employee, name='top_selling_employee'),
    path('api/analytics/top-product/', top_selling_product, name='top_selling_product'),
]
