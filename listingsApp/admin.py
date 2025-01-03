from django.contrib import admin

# Register your models here.
from .models import Category, Product
# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')
  prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'category', 'slug', 'price', 'available')
  list_filter = ('category', 'available')
  list_editable = ('price', 'available')
  prepopulated_fields = {'slug': ('name',)}