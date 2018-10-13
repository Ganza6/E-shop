from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=32,blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return "%s" % (self.name)


class Product(models.Model):
    name = models.CharField(max_length=64,null = True,default= None)#null - запишется null в базу данных при отсутствии значения
    description = models.TextField(blank=True,null = True,default= None)#blank -обязательное поле или нет
    is_active = models.BooleanField(default=True)
    full_description = models.TextField(blank=True,null = True,default= None)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=1000)
    created = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)
    type = models.ForeignKey(ProductType,on_delete=models.CASCADE,null = 1)
    discount = models.IntegerField(default=0,blank=True)
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return "%s %s %s" % (self.price,self.name,self.id)


class ProductImage(models.Model):
    product = models.ForeignKey(Product,blank=True,null = True,default= None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return "Заказ %s" % self.id
