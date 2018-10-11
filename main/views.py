from django.shortcuts import render
from products.models import *
import random
random.seed # ?
def main(request):
    products_images = ProductImage.objects.filter(is_active=True,is_main = True)
    products_images_cups = products_images.filter(product__type__id=2)
    products_images_teapots = products_images.filter(product__type__id=1)  # по захардкоженому ID фильтруют только сотонисты)
    a = len(products_images)-4
    b = random.randint(0,a)
    products_images = products_images[b:b+4]
    print(products_images)
    return render(request, 'main\main.html',locals())  # locals использовать стоит только в исключительных случаях.
    # Контекст стоит перечислить всеь
