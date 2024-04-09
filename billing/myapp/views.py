from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Product, Customer, Bill, BillItem
from .serializers import EmployeeSerializer, ProductSerializer, CustomerSerializer, BillSerializer, BillItemSerializer
from django.shortcuts import get_object_or_404
from django.db import models
from .models import Bill

# Authentication API
@api_view(['POST'])
def generate_token(request):
    # Implementation for generating JWT token
    return Response("JWT token generated successfully", status=status.HTTP_200_OK)

# Employee APIs
@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Product APIs
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Customer APIs
# Implement similar CRUD APIs for Customer as done for Employee and Product

# Billing APIs
# Implement APIs for creating, listing, and retrieving bills, along with bill items

# Analytics APIs
# Implement APIs for retrieving analytics data such as top-selling employee and top-selling product

# Customer APIs
@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Billing APIs
@api_view(['POST', 'GET'])
def bill_list(request):
    if request.method == 'POST':
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)

# Bill Item APIs
@api_view(['POST', 'GET'])
def bill_item_list(request):
    if request.method == 'POST':
        serializer = BillItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        bill_items = BillItem.objects.all()
        serializer = BillItemSerializer(bill_items, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def bill_item_detail(request, bill_item_id):
    bill_item = get_object_or_404(BillItem, id=bill_item_id)
    serializer = BillItemSerializer(bill_item)
    return Response(serializer.data)

# Analytics APIs
@api_view(['GET'])
def top_selling_product(request):
    # Retrieve the product with maximum sales
    top_product = BillItem.objects.values('product_id').annotate(total_sales=models.Sum('quantity')).order_by('-total_sales').first()
    if top_product:
        product = get_object_or_404(Product, id=top_product['product_id'])
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("No sales data available", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def top_selling_employee(request):
    # Retrieve the employee with maximum sales
    top_employee = Bill.objects.values('employee_id').annotate(total_sales=models.Sum('billitem__quantity')).order_by('-total_sales').first()
    if top_employee:
        employee = get_object_or_404(Employee, id=top_employee['employee_id'])
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("No sales data available", status=status.HTTP_404_NOT_FOUND)
