from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProcuctAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProcuctAdmin)
admin.site.register(Category, CategoryAdmin)
