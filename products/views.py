from django.shortcuts import render
from products.models import *

def product(request,product_id):
    product = Product.objects.get(id = product_id) # ты должен позаботится о том, что если я введу ссылку на несуществующий продукт, то
    return render(request, 'product/product.html',locals()) # получу 404, а не 500
