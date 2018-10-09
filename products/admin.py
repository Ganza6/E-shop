from django.contrib import admin
from . models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    class Meta:
        model = Product
    inlines = [ProductImageInline]#can download images from product
admin.site.register(Product,ProductAdmin)

class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductType._meta.fields]
    class Meta:
        model = ProductType
admin.site.register(ProductType,ProductTypeAdmin)

# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductImage._meta.fields]
#     class Meta:
#         model = ProductImage
# admin.site.register(ProductImage,ProductImageAdmin)

