from django.contrib import admin
from .models import *
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_popular', 'created', 'updated', 'available', 'price']
    list_filter = ['is_popular', 'created', 'updated', 'available']
    list_editable = ['price', 'is_popular']
    prepopulated_fields = {'slug': ('name',)}