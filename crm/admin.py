from django.contrib import admin

from .models import Customer, Service, Product, User


class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'organization', 'phone_number' )
    list_filter = ( 'cust_name', 'organization')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


class ServiceList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'service_category', 'setup_time')
    list_filter = ( 'cust_name', 'setup_time')
    search_fields = ('cust_name', )
    ordering = ['cust_name']

class ProductList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'product', 'pickup_time')
    list_filter = ( 'cust_name', 'pickup_time')
    search_fields = ('cust_name', )
    ordering = ['cust_name']

class UserList(admin.ModelAdmin):
    list_display = ( 'username', 'first_name', 'date_joined')
    list_filter = ( 'username', 'date_joined')
    search_fields = ('username', )
    ordering = ['username']


admin.site.register(Customer, CustomerList)
admin.site.register(User, UserList)
admin.site.register(Service, ServiceList)
admin.site.register(Product, ProductList)
