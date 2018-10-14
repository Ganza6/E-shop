from django.db import models
from products.models import Product
from django.db.models.signals import post_save


class Status(models.Model):
    name = models.CharField(max_length=32,blank=True,null = True)
    is_active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    comments = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=2, max_digits=8, default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,limit_choices_to={'is_available': True})
    number = models.IntegerField(default=1)
    price_per_item = models.DecimalField(decimal_places=2, max_digits=7)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.product.name

    def save(self):
        self.price_per_item = self.product.price
        self.total_price = self.price_per_item * self.number
        super().save()

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'


class Customer(models.Model):
    name = models.CharField(max_length=32, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=48, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    test = models.ForeignKey(Order, on_delete=models.CASCADE)#нужно переименовать

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


def product_in_order_post_save(sender,instance,created,**kwargs):#чтобы цена состояла из всех товаров заказа
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save,sender = ProductInOrder)
