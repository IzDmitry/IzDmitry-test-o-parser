from django.contrib import admin
from django.utils.html import format_html
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'display_image',
                    'name', 'price', 'discount']

    def display_image(self, obj):
        return format_html(
            '<img src="{}" style="max-height: 100px; max-width: 100px;"/>'.format(obj.image_url)
            )

    display_image.short_description = 'Image'
