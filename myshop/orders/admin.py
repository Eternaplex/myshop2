from django.contrib import admin
from .models import *

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'city', 'created',]
    list_filter = ['created', 'updated', 'paid']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)