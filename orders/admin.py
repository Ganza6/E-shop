from django.contrib import admin
from . models import Order, ProductInOrder, Customer


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 1
    exclude = ('price_per_item',
               'total_price')


class CustomerInline(admin.TabularInline):
    model = Customer
    max_num = 1
    verbose_name_plural = 'Покупатель'


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    exclude = ('total_price',)
    inlines = [ProductInOrderInline, CustomerInline]

    class Meta:
        model = Order


admin.site.register(Order,OrderAdmin)