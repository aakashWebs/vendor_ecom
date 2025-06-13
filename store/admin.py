from django.contrib import admin
from .models import Category, Product, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor', 'created_at')
    search_fields = ('name', 'vendor__username')
    list_filter = ('created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'vendor', 'price', 'created_at')
    search_fields = ('name', 'category__name', 'vendor__username')
    list_filter = ('category', 'created_at')
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
