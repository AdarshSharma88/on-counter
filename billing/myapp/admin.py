from django.contrib import admin
from .models import Employee, Product, Customer, Bill, BillItem

admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(BillItem)
