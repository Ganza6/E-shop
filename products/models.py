from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64,null = True,default= None)
    description = models.TextField(blank=True,null = True,default= None)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=1000)
    created = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

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
