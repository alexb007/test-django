from django.contrib import admin

from core.models import Category, Review, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_display_links = ('title', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'color', 'price',)
    list_display_links = ('title', 'category', 'color', 'price',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('body', 'product', 'created')
    list_display_links = ('body', 'product', 'created')
